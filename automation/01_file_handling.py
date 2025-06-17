"""
    File Handling
"""

# Write to file 
with open("log.txt", "w") as f:
    f.write("Automation started.\n")

# Append to file 
with open("log.txt", "a") as f:
    f.write("New line added.\n")

# Read from file 
with open("log.txt", "r") as f:
    content = f.read()
    print(content)