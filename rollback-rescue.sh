#!/bin/bash

clear
echo ""
echo "----- Rolling Back Configurations -----"
ansible-playbook -i hosts main.yml -t rollback -e "rollback_rescue='1'" -K
echo ""
echo "----- End of script -----"
echo ""
