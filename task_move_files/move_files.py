"""
 Moves all .txt files from an incoming folder into a processed folder, 
 creating processed if it doesn’t exist:
"""
from pathlib import Path
import shutil

incoming = Path(".")
processed = Path("./moved")

processed.mkdir(exist_ok=True)

for txt_file in incoming.glob("*.txt"):
    dest = processed / txt_file.name
    shutil.move(str(txt_file), str(dest))
    print(f"Moved {txt_file} to {dest}")
