# Playbook Information
## Custom Libraries
* `tasks/roles/compliance/compliance_test.py`     # custom mobule for setting ansible_facts based on compliance tests

## NAPALM Libraries
[napalm-ansible project](https://github.com/napalm-automation/napalm-ansible)
* `tasks/roles/compliance/library/napalm_get_facts.py`
* `tasks/roles/compliance/library/napalm_ping.py`
* `library/napalm_install_config.py`

## Per Device Brown Files
For anything not yet abstracted with goal to abstract.
* `./tasks/roles/base_config/templates/brownfiles/{{ inventory_hostname }}.txt`

## Variables
* `group_vars/all.yml`                           # used to define playbook level variables.
* `tasks/roles/base_base/vars/main.yml`          # currently empty.
* `tasks/roles/base_fabric/vars/main.yml`        # all fabric links.
* `tasks/roles/base_bgp/vars/main.yml`           # all fabric bgp fabric variables.
* `host_vars`                                    # minimal information related to hosts that is not fabric based.

## Templates
All roles start with `base.j2` which then calls the other templates as required.
* `tasks/roles/config_base/templates/`
* `tasks/roles/config_fabric/templates/`
* `tasks/roles/config_bgp/templates/`
* `tasks/roles/config_customer/templates/{{ role }}`
* `tasks/roles/compliance_reports/templates/output.j2`

## Directories
Defined in `./group_vars/all.yml`
* `build/`           # Used only to create device configurations.
* `compiled/`        # Assembled configrations appear here along with diff files.
* `reports/`         # Compliance reports will appear here.
* `reports/debug`    # Compliance report debugs will appear here, both JSON and YAML file formats are generated.
* `.rescue-configs/` # used by rollback-rescue.sh script to return LAB to pre-automated state.

# Running Playbook
## Automated fabric provisioning
1. `rollback-rescue.sh`   # only to reset configurations to management only, no services provisioned.
2. `generate-configs.sh`  # generate the configurations, log into devices and generate diff, no committing done.
3. `deploy-configs.sh`    # deploy configurations and commit changes.

## Automated fabric verification
1. `verify.sh`            # fabric operation verification tests
