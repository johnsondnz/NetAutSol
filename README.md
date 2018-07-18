# NetAutSol
## Brief
Network in configured using *Ansible and NAPALM.*
MPLS network consisting of;
* 8 x Junos Olives in EVE-NG.
Note: *IOS devices shown for reference only*

## Playbook Details
[Playbook Information](https://github.com/johnsondnz/NetAutSol/blob/master/DETAILS.md)

## Homework submissions
- [CHANGELOG](https://github.com/johnsondnz/NetAutSol/blob/master/CHANGELOG.md)

## Todo
- [TODO](https://github.com/johnsondnz/NetAutSol/blob/master/TODO.md)

## Current Objectives
* Provision all services via automated solution.
* Scalability is key, addition of new devices, links, VPNs etc must be easy.
* Verification of network state based on abstracted configuration.
* Network diagram generation based on ISIS protocol advertisements.

## Implimented
- [x] MPLS Fabric and associated core routing protocols.
- [x] mBGP.
- [ ] Layer-2 and Layer-3 VPNs for customer access.
- [ ] Network state verification.
  - [x] IS-IS Adjacencies
  - [x] Ping Tests

# LAB Information
## Network Setup
### P Nodes
* LAB-COR1
* LAB-COR2
* LAB-COR3
* LAB-COR4

### PEs
* LAB-PE1
* LAB-PE2
* LAB-PE3
* LAB-PE4

### Route Reflector Cluster
* LAB-COR1
* LAB-COR2

### Management
em0 on all nodes connected to physical VLAN 22

### Topology
![Topology](https://i.imgur.com/T3AaoIQ.png)
