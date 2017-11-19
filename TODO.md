# Todo
## Role Progress
- [ ] `compliance`               # shows commands and compliance_test fact generation.
- [x] `compliance_reports`       # generates reports from facts `compliance_test_*`.
- [x] `config_base`              # base configurations.
- [x] `config_fabric`            # dynamic mpls fabric.
- [x] `config_bgp`               # dynamic mBGP configuration.
- [x] `config_services`          # dynamic customer interface and routeing-instance provisioning.

## Bugs
* `fabric_interfaces` sub_iface is not currently a parent to the logical items, `inet`, `iso`, `mpls` and `cost`.

## @ip notes:
ip [22:59] 
@Donald @carlbuchmann I got role dependencies to work here https://github.com/ipspace/NetOpsWorkshop/tree/master/Ansible/Roles but also had an interesting troubleshooting session. 

In the end I just listed the names of the role in *dependencies* (and IIRC you have to either use a list of role names, or use list of dictionaries if the elements have more arguments than just the role name).
