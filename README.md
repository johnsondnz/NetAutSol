# NetAutSol
## Brief
MPLS network consisting of;
* 8 x Junos Olives in EVE-NG.
* 6 x C3725
* 2 x vIOS L2

## Current Objectives
* Provision all services via automated solution.
* Scalability is key, addition of new devices, links, VPNs etc must be easy.
* Verification of network state based on abstracted configuration.
* Network diagram generation based on ISIS protocol advertisements.

## Implimented
- [x] MPLS Fabric and associated core routing protocols.
- [ ] MP-BGP.
- [ ] Layer-2 and Layer-3 VPNs for customer access.
- [ ] Network state verification.
  - [x] IS-IS Adjacencies
  - [x] Ping Tests
- [ ] Network diagram generation.

## Network Setup
### P Nodes
* LAB-COR1
* LAB-COR2
* LAB-COR3
* LAB-COR4

### PEs
* LAB-PE1
* LAB-PE2
* LAB-PE3 (Added later to test scalability)
* LAB-PE4 (Added later to test scalability)

### Route Reflector Cluster
* LAB-COR1
* LAB-COR2

### Management
em0 on all nodes connected to physical VLAN 22

### Automation
Network in configured using *Ansible and NAPALM.*

### Topology
![Topology](https://i.imgur.com/J4VCsYK.png)

# Libraries
## Custom Libraries
* `tasks/roles/compliance/compliance_test.py`     # custom mobule for setting ansible_facts based on compliance tests

## NAPALM Libraries
[napalm-ansible project](https://github.com/napalm-automation/napalm-ansible)
* `tasks/roles/compliance/library/napalm_get_facts.py`
* `tasks/roles/compliance/library/napalm_ping.py`
* `library/napalm_install_config.py`

# Playbook Information

## Per Device Brown Files
For anything not yet abstracted with goal to abstract.
* `./tasks/roles/base_config/templates/brownfiles/{{ inventory_hostname }}.txt`

## Roles
* `compliance`               # shows commands and compliance_test fact generation
* `compliance_reports`       # generates reports from facts 'compliance_test_*'
* `config_base`              # base configurations
* `config_bgp`               # dynamic bgp configurations
* `config_fabric`            # dynamic mpls fabric
* `config_customer`          # dynamic customer interface provisioning, includes VLAN-SW, PEs and CEs

## Variables
* `./group_vars/all.yml`                           # used to define playbook level variables.
* `./tasks/roles/base_base/vars/main.yml`          # currently empty.
* `./tasks/roles/base_fabric/vars/main.yml`        # all fabric links.
* `./tasks/roles/base_bgp/vars/main.yml`           # all fabric bgp fabric variables.
* `./host_vars`                                    # minimal information related to hosts that is not fabric based.

## Templates
All roles start with `base.j2` which then calls the other templates as required.
* `./tasks/roles/config_base/templates/`
* `./tasks/roles/config_fabric/templates/`
* `./tasks/roles/config_bgp/templates/`
* `./tasks/roles/config_customer/templates/{{ role }}`
* `./tasks/roles/compliance_reports/templates/output.j2`

## Directories
Defined in `./group_vars/all.yml`
* `./build/`           # Used only to create device configurations.
* `./compiled/`        # Assembled configrations appear here along with diff files.
* `./reports/`         # Operational verification reports will appear here.
* `./.rescue-configs/` # used by rollback-rescue.sh script to return LAB to pre-automated state.

# Running Playbook
## Automated fabric provisioning
1. `./rollback-rescue.sh`   # only to reset configurations to management only, no services provisioned.
2. `./generate-configs.sh`  # generate the configurations, log into devices and generate diff, no committing done.
3. `./deploy-configs.sh`    # deploy configurations and commit changes.

## Automated fabric verification
1. `./verify.sh`            # fabric operation verification tests
