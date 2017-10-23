# NetAutSol
## Brief
Network in configured using *Ansible and NAPALM.*
MPLS network consisting of;
* 8 x Junos Olives in EVE-NG.
* 6 x C3725
* 2 x vIOS L2

## Playbook Details
[Playbook Information](https://github.com/johnsondnz/NetAutSol/blob/master/DETAILS.md)

## Homework submissions
- [Week 1](https://github.com/johnsondnz/NetAutSol/blob/master/weekly_homework_submissions/WEEK1.md)
- [Week 2](https://github.com/johnsondnz/NetAutSol/blob/master/weekly_homework_submissions/WEEK2.md)

## Todo
- [Todo List](https://github.com/johnsondnz/NetAutSol/blob/master/weekly_homework_submissions/todo.md)

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
