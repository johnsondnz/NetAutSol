#!/bin/bash

clear
echo ""
echo "----- Generating Configurations -----"
ansible-playbook -i hosts main.yml -e "commit_changes=0" -K
#find compiled/ -name 'diff' -exec subl {} \;
echo ""
echo ""
echo "----- Configurations and diffs can be found in compiled/ directory -----"
echo "----- Generated Diff files -----"
find compiled/ -name '*.diff' -exec awk 'END { if (NR > 1) print FILENAME }' {} \;
echo ""

echo "----- End of script -----"
echo ""
