import json 

# Write JSON 
data = {"env": "prod", "status":"ok"}
with open("status.json", "w") as f:
    json.dump(data, f)

# Read JSON 
with open("status.json", "r") as f:
    loaded = json.load(f)
    print(loaded) 