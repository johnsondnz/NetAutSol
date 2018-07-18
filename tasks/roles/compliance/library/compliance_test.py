"""
(c) 2017 Donald Johnson <donald@it-ninja.xyz>

This file is part of Ansible

Ansible is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Ansible is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
"""
from ansible.module_utils.basic import AnsibleModule, return_values
import re

DOCUMENTATION = '''

---
module: unit_test
author: "Donald Johnson (@johnsondnz)"
version_added: "0.1"
short_description: "Custom module to decern pass/fail of a specified test and return as ansible facts."
description:
    - "Custom module to decern pass/fail of a specified test and return as ansible facts."
options:
    fact_name: Desired fact name, auto prepended with 'compliance_test_'
    structured_data: JSON key,value data to iterate over - strings not accepted at this time
    string: used instead of structured_data, allows for the search of a phrase within a string
    condition: condition that must be met to 'PASS'
    key: the key to check exists or if value is present
    search: value to look for in either structured_data or string (regex enabled when searching strings)
    test_name: Name of test
    description: Brief description of the unit test

'''

EXAMPLES = '''

# ----- ----- #
- set_fact: test_name=System Alarms
- name: "{{test_name}} Check"
  unit_test:
    fact_name: system_alarms
    test_name: "{{test_name}}"
    description: Check for alarms
    key: no-active-alarms
    data: "{{getter_system_alarms}}"
    condition: key-exists

"ansible_facts": {
    "compliance_test_alarms_system": {
        "search": null,
        "test_name": "System Alarms",
        "conditon": "key-exists",
        "key": "no-active-alarms",
        "test_description": "Check for alarms",
        "test_result": "[FAIL]"
    },
},

# ----- ----- #
- set_fact: test_name=Software
- name: "SRX550 {{test_name}} Check"
  unit_test:
    fact_name: software_version
    test_name: "{{test_name}}"
    description: Check for correct version
    key: os_version
    search: "{{srx550_software_ver}}"
    data: "{{napalm_facts}}"
    condition: key-value-match
  when: "'SRX550' in napalm_model"

"ansible_facts": {
    "compliance_test_software_version": {
        "search": "12.1X44-D35.5",
        "test_name": "Software",
        "conditon": "key-value-match",
        "key": "os_version",
        "test_description": "Check for correct version",
        "test_result": "[PASS]"
    },
},

# ----- ----- #
- set_fact: test_name="Environment"
- name: "{{ test_name }} Check"
  unit_test:
    fact_name: "fan_{{ line_item.name | regex_replace(' ', '_') }}"
    test_name: "{{ test_name }}: {{ line_item.name }}"
    description: Check current status is 'OK'
    key: status
    search: 'OK'
    data: "{{ line_item }}"
    condition: key-value-match
  with_items:
    - "{{ getter_chassis_environment.output[0]['rpc-reply']['environment-information']['environment-item'] }}"
  loop_control:
    loop_var: line_item

"ansible_facts": {
    "compliance_test_fan_srxsme_chassis_fan_0": {
        "search": "OK",
        "test_name": "Environment: SRXSME Chassis Fan 0 Fans",
        "conditon": "key-value-match",
        "key": "status",
        "test_description": "Check current status is 'OK'",
        "test_result": "[PASS]"
    },
    "compliance_test_fan_routing_engine": {
        "search": "OK",
        "test_name": "Environment: Routing Engine Temp",
        "conditon": "key-value-match",
        "key": "status",
        "test_description": "Check current status is 'OK'",
        "test_result": "[FAIL]"
    },
    "compliance_test_fan_srxsme_chassis_fan_2": {
        "search": "OK",
        "test_name": "Environment: SRXSME Chassis Fan 2 Fans",
        "conditon": "key-value-match",
        "key": "status",
        "test_description": "Check current status is 'OK'",
        "test_result": "[PASS]"
    },
}

# ----- ----- #
- set_fact: test_name="IS-IS Adjancency"
- name: "{{ test_name }} Check"
  compliance_test:
    fact_name: isis_adjacency_{{ line_item.interface | regex_replace('/','_') | regex_replace('-','') }}
    test_name: "{{ test_name }}"
    description: Check for IS-IS neighbour on '{{ line_item.interface }}'
    search: "{{ line_item.interface }}.*?Up"
    string: "{{ getter_isis_adjacency.stdout[0] }}"
    condition: unstructured-data-text-search
  with_items:
    - "{{ fabric_tests }}"
  loop_control:
    loop_var: line_item

"ansible_facts": {
    "compliance_test_isis_adjacency_em1": {
        "search": "em1.+?Up",
        "test_name": "IS-IS Adjancency",
        "conditon": "unstructured-data-text-search",
        "key": null,
        "test_description": "Check for IS-IS neighbour on 'em1'",
        "test_result": "[PASS]"
    },
    "compliance_test_isis_adjacency_em0": {
        "search": "em0.+?Up",
        "test_name": "IS-IS Adjancency",
        "conditon": "unstructured-data-text-search",
        "key": null,
        "test_description": "Check for IS-IS neighbour on 'em0'",
        "test_result": "[FAIL]"
    },
}

'''

RETURN = '''

ansible_facts:
    description: "Facts based on test conditions"
    returned: PASS / FAIL
    type: dict

    'compliance_test_' + fact_name: {
        'test_name': test_name,
        'test_description': description,
        'conditon': condition,
        'key': key or null,
        'search': search or null,
        'test_result': test_result
    }

'''


def _recursive_search(data, find_key, *args):
    if find_key in data:
        # print "found %s key" % find_key
        # if a argument is submitted use it to check the located key
        # for a value matching the argument
        # otherwise this was a key-search only
        if args:
            value_search = args[0]
            if value_search in data[find_key]:
                # print "found %s in %s" % (value_search, find_key)
                return True
        else:
            return True
    else:
        for key, value in data.iteritems():
            if isinstance(value, dict):
                # print "%s is a dict" % key
                test = _recursive_search(value, find_key)
                if test is True:
                    return test
            # test for a list
            elif isinstance(value, list):
                # print "%s is a list" % key
                for data in value:
                    # print data
                    if isinstance(data, dict):
                        # print "%s is a dict" % data
                        test = _recursive_search(data, find_key)
                        if test is True:
                            return test
            # can use this later to look at strings
            elif isinstance(value, str):
                # print "%s contains a string" % key
                pass
    return False


def _evaluate_results(recursive_result, invert=False):
    if recursive_result and invert == False:
        test_result = '[PASS]'
    elif recursive_result == False and invert == False:
        test_result = '[FAIL]'
    elif recursive_result == False and invert:
        test_result = '[PASS]'
    elif recursive_result and invert:
        test_result = '[FAIL]'
    return test_result


def _main():
    # define the available arguments/parameters that a user can pass to
    # the module
    module_args = dict(
        fact_name=dict(type='str', required=True),
        test_name=dict(type='str', required=True),
        string=dict(type='str', required=False),
        structured_data=dict(type='dict', required=False),
        condition=dict(type='str', required=True, choices=[
                       'key-exists', 'key-not-exist', 'key-value-match', 'unstructured-data-text-search']),
        key=dict(type='str', required=False),
        search=dict(type='str', required=False),
        description=dict(type='str', required=True),
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Setup easy to reference variables
    fact_name = module.params['fact_name'].lower()
    test_name = module.params['test_name']
    if module.params['structured_data']:
        data = module.params['structured_data']
    elif not module.params['structured_data'] and module.params['string']:
        data = module.params['string']
    condition = module.params['condition']
    key = module.params['key']
    search = module.params['search']
    description = module.params['description']

    # Run the unit test
    new_facts = {}
    if condition in 'key-exists':
        test = _recursive_search(data, key)
        test_result = _evaluate_results(test)

    elif condition == 'key-not-exist':
        test = _recursive_search(data, key)
        test_result = _evaluate_results(test, True)

    elif condition == 'key-value-match':
        test = _recursive_search(data, key, search)
        test_result = _evaluate_results(test)

    elif condition == 'unstructured-data-text-search':
        if re.search(re.compile(search), data) is not None:
            test = True
        else:
            test = False
        test_result = _evaluate_results(test)

    # Create facts object
    new_facts = {
        # prepend compliance_test_ to all facts
        'compliance_test_' + fact_name: {
            'test_name': test_name,
            'test_description': description,
            'conditon': condition,
            'key': key,
            'search': search or None,
            'test_result': test_result
        }
    }
    # Prep the ansible_facts
    results = {'ansible_facts': new_facts}

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        return results

    module.exit_json(**results)


if __name__ == '__main__':
    _main()
