#!/bin/bash

clear
echo ""
echo "----- Deploying Configurations -----"
ansible-playbook -i hosts main.yml -e "commit_changes=1"
echo ""

echo "----- End of script -----"
echo ""
