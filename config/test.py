import os
import subprocess

filename = "../inventory"  # Replace with the actual filename

# Check if the file is empty after removing whitespace and control characters:
with open(filename, "r") as file:
    content = file.read()
    if not content.strip():  # Remove whitespace and check if empty
        output = "Nothing in the Inventory."
    else:
        # Run Ansible command and capture output
        subprocess.run(["ansible", "all", "-m", "ping", "--check"], check=True)
        with open("out.log", "r") as logfile:
            output = logfile.read()

# Append output to GITHUB_OUTPUT environment variable
# os.environ["GITHUB_OUTPUT"] += f"out=({output})"
print(output)
# subprocess.run(["echo", "out=$(cat out.log)", ">>", "$GITHUB_OUTPUT"], check=True)
