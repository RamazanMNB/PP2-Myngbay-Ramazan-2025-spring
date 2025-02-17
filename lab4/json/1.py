
import json

# Load JSON file
with open("lab4/json/sampledata.json") as f:
    data = json.load(f)

# Print table header
print("Interface Status")
print("=" * 65)
print("{:<50} {:<15} {:<5}".format("DN", "Speed", "MTU"))
print("-" * 65)

# Extract and print interface details
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print("{:<50} {:<15} {:<5}".format(dn, speed, mtu))