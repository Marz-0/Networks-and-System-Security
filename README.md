# Networks & Systems Security – Portfolio
**Author:** Marzhan Anbia
**Module:** Networks & Systems Security  
**Institution:** Goldsmiths, University of London  
**Assessment:** E-Portfolio (30%)  
**Semester:** 2024/2025  



## Overview
This portfolio showcases my practical work across the Networks and Systems Security module. Each week includes:

- ✔️ Completed lab tasks  
- ✔️ Python scripts and outputs  
- ✔️ Technical explanations  
- ✔️ Reflections connecting the work to cybersecurity principles  
- ✔️ Evidence of debugging, testing, and iterative improvement  

The aim of this portfolio is to demonstrate a **clear and technically sound understanding** of security fundamentals, including cryptography, network scanning, system hardening, incident analysis, secure communication protocols, penetration testing and generative AI (LLM) pen testing.

This repository follows a weekly logbook structure to show my progression from foundational tasks to more advanced security implementations.



## 📂 Repository Structure

```
/
├── Lab 1/
│   └── Lab 1.pdf
├── Lab 2/
│   ├── generate_keys.py
│   ├── sender_client.py
│   ├── Server_receiver.py
│   └── Peer_Reflection_summary.md
│   └── Lab_2_Summary.md
├── Lab 3/
│   ├── 2FA.py
│   ├── authentication_class.py
│   ├── Brute_force.py
│   ├── hashing.py
│   ├── password_checker.py
│   ├── salt_pepper.py
│   └── Lab_3_Summary.md
├── Lab 4/
│   └── Files/
│       ├── file1.txt
│       ├── file2.txt
│       ├── file3.txt
│   ├── baseline.csv
│   ├── connections.csv
│   ├── file_integrity_baseline.py
│   ├── file_integrity_check.py
│   ├── malware_detect.py
│   ├── Network_monitor.py
│   ├── SHAalgo.py
│   ├── Worm_scan.py
│   └── Lab_4_Summary.md
├── Lab 5/
│   ├── web_security.py
│   └── Lab_5_Summary.md
├── Lab 6/
│   ├── binary_analysis.py
│   ├── hash_calc.py
│   ├── ioc_yara.py
│   ├── pe_header_inspect.py
│   ├── string_extraction.py
│   └── Lab_6_summary.md
├── Lab 7/
│   ├── Nmap.py
│   ├── Pen_test.py
│   ├── Port_scanner.py
│   ├── Whois_domain_lookup.py
│   └── Lab_7_summary.md
├── Lab 9/
│   ├──
│   └── reflection.md
├── package-lock.json
├── package.json
├── private_key.pem
├── public_key.pem
├── totp_qr.marz.png
├── totp_qr.png
└── README.md
```


## Learning Objectives Demonstrated

### 1. Cryptographic Principles  
- RSA key generation  
- Secure hybrid encryption (RSA + AES)  
- Understanding confidentiality, integrity, key exchange, and padding schemes  

### 2. Network Security & Scanning  
- TCP/UDP port scanning  
- WHOIS domain intelligence  
- Enumerating services during reconnaissance  

### 3. Packet & Protocol Analysis  
- Analysing packet flow and port states  
- Understanding TCP vs UDP behaviour  

### 4. System & Binary Security  
- Hashing algorithms (MD5, SHA1, SHA256)  
- String extraction from executables  
- Fundamentals of malware triage  

### 5. Security Architecture & Hardening  
- Firewall rulesets  
- OS-level defensive configurations  
- Threat identification and mitigation  

---

## Weekly Reflection Highlights

### **Week 2 — Hybrid Cryptography & Secure Communication**
Implementing RSA + AES solidified my understanding of hybrid encryption. Debugging socket transmission issues taught me about message framing and reliability.

### **Week 3 — Network Scanning**
Writing a port scanner taught me how TCP handshakes reveal port states. I also learned how filtered ports behave under different firewall conditions.

### **Week 6 — Binary & Malware Analysis**
Extracting hashes and strings showed me how malware analysts triage unknown executables quickly using lightweight static analysis tools.

---

## Evidence of Technical Growth
Examples include:

- Handling network timeouts and socket errors  
- Testing different encryption/decryption scenarios  
- Identifying potential vulnerabilities  
- Improving script modularity and reusability  

---

## Challenges & Solutions

### ❗ Socket Issues
Encrypted messages arrived partially; I fixed it by implementing buffered chunk reading.

### ❗ Binary Handling
Large file crashes led me to implement safer buffered reading techniques.

### ❗ Scan Timeouts
Investigating silent drops helped me understand firewall behaviour and TCP retransmissions.

---

## Alignment with Assessment Criteria
This portfolio demonstrates:

- ✔️ Clear, structured documentation  
- ✔️ Correct and technically sound implementations  
- ✔️ Analytical reflections  
- ✔️ Professional presentation  

---

## Final Statement
This portfolio reflects my progression through applied cybersecurity tasks, growing from foundational experiments to more advanced cryptographic, network, and system-level security work. It demonstrates both technical skill and reflective understanding of core security principles.

