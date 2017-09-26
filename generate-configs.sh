#!/bin/bash

echo ""
echo "----- Generating Configurations -----"
ansible-playbook -i hosts main.yml -e "commit_changes=0"
#find compiled/ -name 'diff' -exec subl {} \;
echo ""
echo ""
echo "Configurations and diffs can be found in compiled/ directory"
echo ""

echo "Generated Diff files"
echo "--------------------"
find compiled/ -name 'diff' -exec awk 'END { if (NR > 1) print FILENAME }' {} \;

echo ""
echo "The best editor for viewing is sublime-text-3 ( https://www.sublimetext.com/3 )"
echo ""
echo "----- End of script -----"
echo ""