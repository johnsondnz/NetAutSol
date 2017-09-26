#!/bin/bash

echo ""
echo "----- Stating Verification Tasks -----"
ansible-playbook -i hosts operations-verify.yml
echo ""
echo "Checking for 'FAIL' items"
grep --colour=always FAIL reports/*
echo ""
echo "----- End of script -----"
echo ""