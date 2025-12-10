import re
import yara

# pip install yara-python
sample = r"C:\Users\Marzhan\Downloads\ProcessMonitor\Procmon.exe"

print("=== POTENTIAL IOCs (URLs and IPs) ===")

# Decode whole file (best effort)
decoded = open(sample, "rb").read().decode(errors="ignore")

# Regex for URLs and IPv4 addresses
url_pattern = r"https?://[^\s\"']+"
ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

urls = re.findall(url_pattern, decoded)
ips = re.findall(ip_pattern, decoded)

print("URLs found:")
for u in urls:
    print(" -", u)

print("\nIP addresses found:")
for ip in ips:
    print(" -", ip)

print("\n=== YARA ANALYSIS ===")

rule_source = """
rule ContainsHTTP {
    strings:
        $s = "http"
    condition:
        $s
}
"""

rules = yara.compile(source=rule_source)
matches = rules.match(sample)
print("YARA matches:", matches)
