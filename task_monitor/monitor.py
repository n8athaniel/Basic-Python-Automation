import time 
from pathlib import Path

folder = Path(".")
seen_files = set()

max_new = 3
new_file_count = 0
stop = False

print(f"Monitoring for new .txt files in '{folder}'")

start_time = time.time()

while not stop and (time.time() - start_time < 30):
    for file in folder.glob("*.txt"):
        if file.name not in seen_files:
            print(f"New file detected: {file.name}")
            seen_files.add(file.name)
            new_file_count += 1

            if new_file_count >= max_new:
                print("\nDetected maximum number of files. Exiting.")
                break
    time.sleep(5) 

print("\nDone")