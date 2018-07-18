# Interim Changes
## Based on week 4 feeback from Ivan
* migrated away from shell scripts.
* created new top level plays `./play_*.yml`.
* removed most tags.
* aggragted many `./tasks/*.yml` files.
* moved `/.tasks/assemble_push_config/yml` into two new roles:
  * `napalm_assemble_configs`.
  * `napalm_deploy_configs`.
* created role depenecies to simplify role triggering.
* check_mode can be used to prevent deviceconfiguration deployment in `./roles/napalm_deploy_configs/tasks.main.yml`.
  * doing so will also prevent `compliance*` roles from triggering.
* removed all reference *when: commit_changes | match('0')* in tasks, now utilising check_mode.
* cleanup of `./group_vars/all.yml`.
* `./.gitignore` now omits `./reports` and `./compiled` directories.
* added some config examples.
* renamed `./hosts/` to `./inventory`.
* multiple role calling tasks now exist. `./tasks/role_*.yml`.

# WEEK 4
## Services Data Model (as defined in Week 3)
* defined data models in [config_services](https://github.com/johnsondnz/NetAutSol/tree/master/vars).
  * added datamodel `./tasks/roles/config_services/vars/services_vpnv4.yml`
  * added datamodel `./tasks/roles/config_services/vars/services_l2vpn.yml`
  
## Changes
* Moved all role variables into root `./vars/`, with the exception of dynamically generated facts.
  * Moved `./tasks/roles/config_fabric/vars/main.yml` to `./vars/config_fabric.yml`.
  * Moved `./tasks/roles/config_services/*.yml` to `./vars/*.yml`.
  * Updated `./main.yml` to import all variables from `./vars` using fileglob
  * Deleted `./tasks/roles/config_base/vars/` directory, main.yml was empty.
  * Deleted `./tasks/roles/config_services/vars/`, directory was empty.
* Enabled previously commented out cleanup task in `./tasks/roles/compliance/tasks/tests/verify-ping.yml`.
* Removed the Cisco IOS devices, objective changed to automate a Junos MPLS fabric.
  * I was biting off more than I could chew.
  * Diagram not yet updated.
  * Deleted `./host_vars/` files related to IOS devices.
* Moved `./weekly_homework_submissions/todo.md` to `./TODO.md`.
* Minor updates to `./README.md`.
* Removed dynamic diagram generation as an objective.
* Updated `./DETAILS.md` to reflect new variable file usage.
* Added tasks for role `config_services` to `./tasks/def_roles.yml`.  This will configure customer services.
* Removed duplicated include of `./tasks/clearnup.yml` task from `./main.yml`.
* Updated `./tasks/hostfile.yml`.  now updated `~/.hosts` which is imported dnsmasq on start.
  * Tasks also restarts dnsmasq to effect changes.
* Removed OSPF from fabric, changed to purely ISIS IGP.
* Added *#jinja2: lstrip_blocks: "True"* to all jinja2 templates to handle indents
* Added task to remove all lines from candidate configurations that start with '#' prior to deploying with napalm.
* Added *Bugs* heading to `./TODO.md`.
* Imported latest code from from [napalm-ansible](https://github.com/napalm-automation/napalm-ansible) for compatibility with new napalm version.
  * `./library/napalm_install_config.py` 
  * `./tasks/roles/compliance/library/napalm_get_facts.py`
  * `./tasks/roles/compliance/library/napalm_ping.py`
* Updated BGP TODO item to completed.
* Added *replace_config=true* to `./tasks/assemble_push_conf.yml` due to extra knob now being required for idempotent configurations with napalm.

## Newly implimented
* Added brownfiles to role `./tasks/roles/config_base`.  Those items which are not yet automated.  (There should be none!)
* Added BGP templates and tasks to `./tasks/roles/config_fabric/` role.  This is to prepare the network for VPN customers.
* Dynamic `vars` for roles.  Cleanup tasks commented out to show examples such as
  * Fabric data model to device data models. `./tasks/roles/device_datamodel/vars/`.
  * Compliance testing models. `./tasks/roles/compliance/vars/`
* New role `./tasks/roles/config_bgp/` for configuring BGP clients and router reflectors.
  * Makes uses of the `bgp_config` fact.
  * Dynamically configures BGP peers for the fabric with the only attributes required being the route reflector node names and ASN.
  * Defines CLIENTS, INTERNAL and REFLECTOR-PEER stanzas.
* Merged all WEEK*.md files into [CHANGELOG.md](https://github.com/johnsondnz/NetAutSol/tree/master/CHANGELOG.md).
  * Deleted `./weekly_homework_submissions` directory.
* Created new role `./tasks/roles/device_datamodel` to create per device data model.
  * Role `./tasks/roles/config_base/` has dependency on this new role using `meta/main.yml`.
  * Previously the jinja2 templates created fabric config from `./vars/config_fabric.yml` model directly.
  * Transitioned all jinja2 templates to make use of the per device data model.

# WEEK 3
## Changes
* Fixed file names for `./tasks/roles/config_services/vars/*.yml` - spelling error corrected.
* Corrected diagrams vlan_ids for CE-PE peering.
  * vlan_id second digit now corresponds correctly to match the PE number.
  * 11xx = PE1
  * 12xx = PE2
  * 13xx = PE3
  * 14xx = PE4
* Updated todo.md - fixed roles name not matching implimentation.

## Newly implimented
* defined data models in [config_services](https://github.com/johnsondnz/NetAutSol/tree/master/tasks/roles/config_services/vars) role.
  * added datamodel `./tasks/roles/config_services/vars/services_vpnv4.yml`
  * added datamodel `./tasks/roles/config_services/vars/services_l2vpn.yml`

# WEEK 2
## Easy Wins

### New Roles
* [tasks/roles/compliance](https://github.com/johnsondnz/NetAutSol/tree/master/tasks/roles/compliance)
* [tasks/roles/compliance_reports](https://github.com/johnsondnz/NetAutSol/tree/master/tasks/roles/compliance_reports)

### New Plays
* [tasks/compliance_play.yml](https://github.com/johnsondnz/NetAutSol/blob/master/tasks/compliance_play.yml)
  * Inherits `compliance` and `compliance_report` roles.

### Compliance Role
* [verify.sh](https://github.com/johnsondnz/NetAutSol/blob/master/verify.sh) will call [tasks/compliance_play.yml](https://github.com/johnsondnz/NetAutSol/blob/master/tasks/compliance_play.yml).
* `tasks/compliance_play.yml` triggers the roles `compliance` and `compliance_reports`.
* The play uses `include_vars` to import variables from the `config_fabric` role.  
  * [tasks/roles/config_fabric/vars/main.yml](https://github.com/johnsondnz/NetAutSol/blob/master/tasks/roles/config_fabric/vars/main.yml)
* A custom module I wrote called [tasks/roles/compliance/library/compliance_test.py](https://github.com/johnsondnz/NetAutSol/blob/master/tasks/roles/compliance/library/compliance_test.py).
  * Used to standardise compliance testing it allows for key-value search with recursive search of structured data or;
  * python re.search of unstructured data.
  * results are standardised and prefix with `compliance_test_` before being returned as ansible_facts.
    * the module returns ansible_facts for use later in report generation.
  * usage examples and returned facts are provided in the module.
* Compliance tests:
  * `tasks/roles/config_fabric/vars/main.yml` is used to generate an ansible_facts dictionary called `fabric_tests`.
    * `fabric_tests` is a list of dictionarys.
    * `{'ping_test': ip_address, 'interface': interface}`
  * `show isis adjacency` is executed on the Junos Olives
  * `fabric_tests.interface` is used as a re.search to look for the interface in an 'Up' state, i.e. 'em1.*?Up'
  * `fabric_tests.ping_dest` is passed to `naplam_ping` with results stored in `ping_results`
  * `ping_results` is passed to `compliance_test` module and results ouput standardised into ansible_facts.

### Tasks
- [tasks/roles/compliance/tasks/main.yml](https://github.com/johnsondnz/NetAutSol/blob/master/tasks/roles/compliance/tasks/main.yml)
  - Dynamically includes `getter` and `test` modules.
  - [tasks/roles/compliance/tasks/getters/](https://github.com/johnsondnz/NetAutSol/tree/master/tasks/roles/compliance/tasks/getters)
    - Information gathering tasks.
  - [tasks/roles/compliance/tasks/tests/](https://github.com/johnsondnz/NetAutSol/tree/master/tasks/roles/compliance/tasks/tests)
    - Compliance tasks which make use of the custom module [tasks/roles/compliance/library/compliance_test.py](https://github.com/johnsondnz/NetAutSol/blob/master/tasks/roles/compliance/library/compliance_test.py).
- [tasks/roles/compliance_reports/tasks/main.yml](https://github.com/johnsondnz/NetAutSol/blob/master/tasks/roles/compliance_reports/tasks/main.yml)
  - Dynamically calls the ordered tasks in [tasks/roles/compliance_reports/tasks/includes/](https://github.com/johnsondnz/NetAutSol/tree/master/tasks/roles/compliance_reports/tasks/includes)
  - Each tasks file is prefixed with a index to esnure order of operation is as expected for report generation

### Compliance Reporting Role
* Triggered with running [verify.sh](https://github.com/johnsondnz/NetAutSol/blob/master/verify.sh).
* Play creates [reports](https://github.com/johnsondnz/NetAutSol/tree/master/reports) directory.
  * subdirectories `build` and `debug` are also created.
* Report header and contents are generated from the role [tasks/roles/compliance_reports/templates](https://github.com/johnsondnz/NetAutSol/tree/master/tasks/roles/compliance_reports/templates) templates.
  * A report header is created for each host and placed into `reports/build/{{ inventory_hostanme }}`
  * Report content is created for each host and placed into `reports/build/{{ inventory_hostanme }}`
  * Report content is generated by looping through the ansible_facts prefixed with `compliance_test_` and passing it to `tasks/roles/compliance_reports/templates/output.j2`
* Assemble module is used to combine the header and report contents
* Each hosts assembled a report is placed into `reports`
* Summary report information is placed at the end of each host report, including passed and failed test counts.
* An aggregated report is generated combining all hosts into a MEGA report, it too is placed into `reports`
* Debugging information is saved to [reports/debug](https://github.com/johnsondnz/NetAutSol/tree/master/reports/debug) in JSON and YAML format.
* The last output is a search of generated reports (excluding the aggregated one) using bash and grep.  Script searches for `'[FAIL]'`, matches are printed to stdout

### Examples
- [examples/00-full-report.txt](https://github.com/johnsondnz/NetAutSol/blob/master/examples/00-full-report.txt)
- [examples/DEPLOY-OUTPUT.md](https://github.com/johnsondnz/NetAutSol/blob/master/examples/DEPLOY-OUTPUT.md)
- [examples/GENERATE-OUTPUT.md](https://github.com/johnsondnz/NetAutSol/blob/master/examples/GENERATE-OUTPUT.md)
- [examples/ROLLBACK-OUTPUT.md](https://github.com/johnsondnz/NetAutSol/blob/master/examples/ROLLBACK-OUTPUT.md)
- [examples/VERIFY-OUTPUT.md](https://github.com/johnsondnz/NetAutSol/blob/master/examples/VERIFY-OUTPUT.md)

# WEEK 1
## Getting Started
- [Playbook Information](https://github.com/johnsondnz/NetAutSol/blob/master/DETAILS.md)

Uploaded (with a few tweaks) a play that I had been playing with since doing the Ansible for Network Enngeerss webinar.

### Roles
* [tasks/roles/config_base](https://github.com/johnsondnz/NetAutSol/tree/master/tasks/roles/config_base)
* [tasks/roles/config_fabric](https://github.com/johnsondnz/NetAutSol/tree/master/tasks/roles/config_fabric)
  * vars/main.yml is used to create the fabric and later also check for compliance.

### New Plays
* [main.yml](https://github.com/johnsondnz/NetAutSol/blob/master/main.yml)
  * Generates or deploys configurations
  * Can rollback configurations to rescue configurations as stored in [.rescue-configs](https://github.com/johnsondnz/NetAutSol/tree/master/.rescue-configs)
