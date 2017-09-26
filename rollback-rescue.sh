#!/bin/bash

echo ""
echo "----- Rolling Back Configurations -----"
ansible-playbook -i hosts main.yml -t rollback -e "rollback_rescue='1'"
echo ""
echo "----- End of script -----"
echo ""