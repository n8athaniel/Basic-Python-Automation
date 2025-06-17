import os
import datetime
import tarfile
import sys

""" 
    python backup.py /path/to/source /path/to/backup_folder
"""

def backup_dir(sorce_dir, destination_dir):
    if not os.path.isdir(sorce_dir):
        print(f"Source dir '{sorce_dir} does not exist.")
        return
    
    if not os.path.isdir(destination_dir):
        print(f"Source dir '{destination_dir} does not exist.")
        return

    timestap = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestap}.tar.gz"
    backup_path = os.path.join(destination_dir, backup_name)

    with tarfile.open(backup_path, "w:gz") as tar:
        tar.add(sorce_dir, arcname=os.path.basename(sorce_dir))
        print(f"Backup vreated: {backup_path}")
    
    if __name__ == "__main__":
        if len(sys.argv) != 3:
            print("Use: python backup.py <sorce_dir> <destination_dir>")
            sys.exit(1)
        
        src = sys.argv[1]
        dest = sys.argv[2]
        backup_dir(src, dest)