# NetAutSol

## Brief
MPLS network consisting of 6 x Junos Olives in EVE-NG.

## Current Objectives
* Provision all services via automated solution.
* Scalability is key, addition of new devices, links, VPNs etc must be easy.

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

## Drawing
![Topology](https://i.imgur.com/fTlCm8y.png)
