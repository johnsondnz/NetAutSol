#!/bin/bash

clear
echo ""
echo "----- Rolling Back Configurations -----"
ansible-playbook -i hosts main.yml -t rollback -e "rollback_rescue='1'" -K
echo ""

echo ""
echo "----- Generating Configurations -----"
ansible-playbook -i hosts main.yml -e "commit_changes=0" -K
#find compiled/ -name 'diff' -exec subl {} \;
echo ""

echo ""
echo "----- Deploying Configurations -----"
ansible-playbook -i hosts main.yml -e "commit_changes=1" -K
echo ""

echo "----- End of script -----"
echo ""
