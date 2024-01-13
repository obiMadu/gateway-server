import os
import subprocess
import re

filename = "../inventory"  # Replace with the actual filename

# Check if the file is empty after removing whitespace and control characters:
with open(filename, "r") as file:
    # content = file.read()
    # print("Inventory file content: " + "'" + content + "'")
    if ( re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", file.readline().strip()) ):  # Check if content matches an IPAddress
        # Run Ansible command and capture output
        subprocess.run(["ansible", "all", "-m", "ping", "--check"], check=True)
        with open("out.log", "r") as logfile:
            output = logfile.read()
    else:
        output = "No valid target in the Inventory."        

# Append output to GITHUB_OUTPUT environment variable
os.environ["GITHUB_OUTPUT"] += f"out=({output})"
print( "Ansible Log Output: " + output)
# subprocess.run(["echo", "out=$(cat out.log)", ">>", "$GITHUB_OUTPUT"], check=True)
