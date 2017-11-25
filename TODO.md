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
