#!/bin/sh

filename="../inventory"  # Replace with the actual filename

regex_pattern="^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"  # Example regex for IPv4 address

if [[ "$(cat "$filename")" =~ $regex_pattern ]]; then
    ansible all -m ping --check;
    echo "out=$(cat out.log)" >> $GITHUB_OUTPUT;
else
    echo "out=$(echo 'Nothing in the Inventory.')" >> $GITHUB_OUTPUT; 
fi
