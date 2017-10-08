# Getting Started
- [Playbook Information](https://github.com/johnsondnz/NetAutSol/blob/master/DETAILS.md)

Uploaded (with a few tweaks) a play that I had been playing with since doing the Ansible for Network Enngeerss webinar.

## Roles
* [config_base](https://github.com/johnsondnz/NetAutSol/tree/master/tasks/roles/config_base)
* [config_fabric](https://github.com/johnsondnz/NetAutSol/tree/master/tasks/roles/config_fabric)
  * vars/main.yml is used to create the fabric and later also check for compliance.

## New Plays
* [main.yml](https://github.com/johnsondnz/NetAutSol/blob/master/main.yml)
  * Generates or deploys configurations
  * Can rollback configurations to rescue configurations as stored in `./.rescue-configs/{{ os }}/`