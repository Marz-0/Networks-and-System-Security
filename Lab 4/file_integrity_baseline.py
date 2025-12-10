# file_integrity_baseline.py
import os
import hashlib
import csv
from datetime import datetime

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER_TO_MONITOR = os.path.join(SCRIPT_DIR, "Files")
BASELINE_FILE = os.path.join(SCRIPT_DIR, "baseline.csv")

def hash_file(path):
    """Return SHA-256 hex digest of a file."""
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha.update(chunk)
    return sha.hexdigest()

def create_baseline():
    # make sure folder exists
    if not os.path.isdir(FOLDER_TO_MONITOR):
        print(f"Folder '{FOLDER_TO_MONITOR}' does not exist.")
        return

    with open(BASELINE_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["filename", "sha256", "timestamp"])

        for name in os.listdir(FOLDER_TO_MONITOR):
            full_path = os.path.join(FOLDER_TO_MONITOR, name)
            if os.path.isfile(full_path):
                file_hash = hash_file(full_path)
                timestamp = datetime.now().isoformat(timespec="seconds")
                writer.writerow([name, file_hash, timestamp])
                print(f"Hashed {name}")

    print(f"\nBaseline written to {BASELINE_FILE}")

if __name__ == "__main__":
    create_baseline()

