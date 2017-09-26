# NetAutSol
## Brief
MPLS network consisting of 6 x Junos Olives in EVE-NG.

## Current Objectives
* Provision all services via automated solution.
* Scalability is key, addition of new devices, links, VPNs etc must be easy.
* Verification of desired network state based on abstracted configuration.
* Network diagram generation based on ISIS protocol advertisements.

## Implimented
- [x] Link Fabric and associated routing protocols.
- [ ] BGP.
- [ ] VPNs / Customer Access.
- [ ] Network state verification.
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
  * Not pictured in the topology

### Route Reflector Cluster
* LAB-COR1
* LAB-COR2

### Management
em0 on all nodes connected to physical VLAN 22

### Automation
Network in configured using *Ansible and NAPALM.*

### Topology
![Topology](https://i.imgur.com/fTlCm8y.png)

# Playbook Information
## Per Device Brown Files
For anything not yet abstracted with goal to abstract.
* `./tasks/roles/base_config/templates/brownfiles/{{ inventory_hostname }}.txt`

## Variables
* `./group_vars/all.yml`                                 # used to define playbook level variables.
* `./tasks/roles/base_config/base_config/vars/main.yml`  # currently empty.
* `./tasks/roles/base_config/fabric/vars/main.yml`       # all fabric links.
* `./tasks/roles/base_config/bgp_speaker/vars/main.yml`  # all fabric bgp fabric variables.
* `./host_vars`                                          # minimal information related to hosts that is not fabric based.

## Templates
All roles start with `base.j2` which then calls the other templates as required.
* `./tasks/roles/base_config/base_config/templates/`
* `./tasks/roles/base_config/fabric/templates/`
* `./tasks/roles/base_config/bgp_speaker/templates/`
* `./templates/`                                          # Used soley for operations verification.

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
1. `./verify.sh`            # currently verifies ISIS protocol only.
