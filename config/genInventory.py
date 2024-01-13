import os
import subprocess

# Change directory to '../deploy'
os.chdir("../deploy")

# Execute Terraform command and capture output
try:
    gate_ip = subprocess.check_output(["terraform", "output", "--raw", "gate_ip"], text=True).strip()
except subprocess.CalledProcessError as error:
    print(f"Error executing Terraform command: {error}")
    exit(1)  # Exit with error code

# Write gate_ip to the inventory file
with open("../inventory", "w") as file:
    file.write(gate_ip)
    print("Inventory Contents: " + gate_ip)