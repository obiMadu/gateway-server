#!/bin/bash

filename="../inventory"  # Replace with the actual filename

# Using 'cat' and checking for empty output:
if [ -z "$(cat "$filename" | tr -d '[:space:]')" ]; then
  echo "out=$(echo 'Nothing in the Inventory.')" >> "$GITHUB_OUTPUT"; 
else
    ansible all -m ping --check;
    echo "out=$(cat out.log)" >> "$GITHUB_OUTPUT";
fi