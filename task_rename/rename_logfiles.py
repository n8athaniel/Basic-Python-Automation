"""
    Write a script that finds all .log files in the current 
    directory and renames them to filename_ARCHIVED.log.
    + if it skips files that are already renamed.
"""
from pathlib import Path 
import os

def rename(file):
    if file.endswith("_ARCHIVED.log"):
        print({f"Skipping already archived file: {file}"})
        return
    
    new_name = file.replace(".log", "_ARCHIVED.log")
    Path(file).rename(new_name)
    print(f"Renamed: {file} -> {new_name}")

files = os.listdir(".")
for file in files:
    if file.endswith(".log"):
        rename(file)
