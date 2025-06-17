# Create a dictionary {"host": "localhost", "port": 8080}, 
# write it to a file config.json, then read it back and print it.

import json 

# Write JSON 
data = {"host": "localhost", "port": 8080}
with open("status.json", "w") as f:
    json.dump(data, f)

# Read JSON 
with open("status.json", "r") as f:
    loaded = json.load(f)
    print(loaded)