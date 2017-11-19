#!/bin/bash

clear
echo ""
echo "----- Stating Verification Tasks -----"
ansible-playbook -i hosts tasks/compliance_play.yml
echo ""
echo "----- Checking reports/*.txt for '[FAIL]' items -----"
grep --colour=always '\[FAIL]' reports/*.txt | grep -v 00-
echo ""
echo "----- End of script -----"
echo ""