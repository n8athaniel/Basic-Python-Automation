# Write a script that creates a directory called backups and writes a 
# file called note.txt inside it with the content "Backup completed."

from pathlib import Path 

# Creates 'backups' if it doesn't exist
backup_dir = Path("backups")
backup_dir.mkdir(exist_ok=True)

# Creates/updates notes.txt inside 'backups'
note_path = backup_dir / "notes.txt"
note_path.write_text("Backup completed.")