import subprocess
from datetime import datetime

servers = ["localhost", "8.8.8.8", "BRo"]
status = {}

for server in servers: 
    result = subprocess.run(f"ping -n 1 {server}",
                            capture_output=True, text=True, shell=True)
    
    if result.returncode == 0: 
        status[server] = "is online"
    else:
        status[server] = "is offline"
    
print(status)

with open("alerts.txt", "w") as f:
    for server, stat in status.items(): 
        f.write(f"{server}: {stat}\n")