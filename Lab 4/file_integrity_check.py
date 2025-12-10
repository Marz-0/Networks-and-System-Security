# file_integrity_check.py
import os
import hashlib
import csv

FOLDER_TO_MONITOR = "Files"
BASELINE_FILE = "baseline.csv"

def hash_file(path):
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha.update(chunk)
    return sha.hexdigest()

def load_baseline():
    baseline = {}
    try:
        with open(BASELINE_FILE, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                baseline[row["filename"]] = row["sha256"]
    except FileNotFoundError:
        print(f"Baseline file '{BASELINE_FILE}' not found. Run file_integrity_baseline.py first.")
        return None
    return baseline

def check_changes():
    baseline = load_baseline()
    if baseline is None:
        return

    current_files = {}

    if not os.path.isdir(FOLDER_TO_MONITOR):
        print(f"Folder '{FOLDER_TO_MONITOR}' does not exist.")
        return

    # Hash current files
    for name in os.listdir(FOLDER_TO_MONITOR):
        full_path = os.path.join(FOLDER_TO_MONITOR, name)
        if os.path.isfile(full_path):
            current_files[name] = hash_file(full_path)

    # Compare with baseline
    print("=== Changes compared to baseline ===")
    for name, current_hash in current_files.items():
        if name not in baseline:
            print(f"[NEW]      {name}")
        elif baseline[name] != current_hash:
            print(f"[MODIFIED] {name}")
        else:
            print(f"[OK]       {name}")

    # Check for missing files
    for name in baseline.keys():
        if name not in current_files:
            print(f"[MISSING]  {name}")

if __name__ == "__main__":
    check_changes()
