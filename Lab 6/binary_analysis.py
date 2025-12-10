# Binary_analysis.py
# This script calls all separate analysis modules for the Week 6 lab.

print("===================================")
print("   WEEK 06 BINARY ANALYSIS REPORT  ")
print("===================================\n")

# 1. Hash calculation
print(">> Running hash calculation...")
import hash_calc
print("\n")

# 2. String extraction
print(">> Extracting readable strings...")
import string_extraction
print("\n")

# 3. PE header inspection
print(">> Inspecting PE headers and imports...")
import pe_header_inspect
print("\n")

# 4. IOC extraction + YARA rule matching
print(">> Running IOC extraction and YARA analysis...")
import ioc_yara
print("\n")

print("===================================")
print("   ANALYSIS COMPLETE ✔")
print("===================================")
