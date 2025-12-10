# network_monitor.py
import csv
from collections import defaultdict

LOG_FILE = "connections.csv"
THRESHOLD = 10  # alert if a host makes more than this many connections

def analyse_connections():
    counts = defaultdict(int)

    try:
        with open(LOG_FILE, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                src_ip = row.get("src_ip")
                if src_ip:
                    counts[src_ip] += 1
    except FileNotFoundError:
        print(f"Log file '{LOG_FILE}' not found.")
        return

    print("=== Connection counts per source IP ===")
    for ip, count in counts.items():
        status = "OK"
        if count > THRESHOLD:
            status = "ALERT: possible scanning / worm activity"
        print(f"{ip}: {count} connections -> {status}")

if __name__ == "__main__":
    analyse_connections()
