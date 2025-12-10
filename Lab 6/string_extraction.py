import re

# Same sample file
sample = r"C:\Users\Marzhan\Downloads\ProcessMonitor\Procmon.exe"

def extract_strings(path):
    with open(path, "rb") as f:
        data = f.read()
    # Printable ASCII strings of length >= 4
    pattern = rb"[ -~]{4,}"
    return re.findall(pattern, data)

strings = extract_strings(sample)

print("=== FIRST 20 STRINGS ===")
for s in strings[:20]:
    print(s.decode(errors="ignore"))
