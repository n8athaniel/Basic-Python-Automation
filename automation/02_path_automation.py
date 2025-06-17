"""
    OS & Path Automation 
"""

import os
from pathlib import Path 

# Make dir
os.makedirs("logs", exist_ok=True)

# List files in a dir
files = os.listdir(".")
print(files)

# Using pathlib for safe path joining 
log_path = Path("logs") / "output.log"
print(log_path)


# NOTES 
"""
exist_ok=True : Don’t throw an error if the folder already exists.
"""