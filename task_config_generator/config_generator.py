import json 
import subprocess

config_dic = {
    "service": "webapp", 
    "host": "localhost",
    "port": 5000
}

with open("config.json", "w") as f:
    json.dump(config_dic, f)

servers = ["localhost", "8.8.8.8", "does-not-exist"]
status = {}

for server in servers:
    result = subprocess.run(f"ping -n 1 {server}", 
                            capture_output=True, text=True, shell=True)
    
    if result.returncode == 0:
        status[server] = "is online"
    else:
        status[server] = "is offline"
    
with open("status.json", "w") as f:
    json.dump(status, f)

with open("status.json", "r") as f:
    loaded = json.load(f)
    print(loaded)