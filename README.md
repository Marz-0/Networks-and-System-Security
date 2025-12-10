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
│   ├── server_receiver.py
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
│   ├── Data_poinsoning.py
│   ├── gemma3.py
│   ├── LLM_findings.md
│   ├── LLM_model.py
│   ├── Model_extraction.py
│   ├── Model_inversion.py
│   ├── Prompt_injection.py
│   ├── qwen7b.py
│   ├── Part_IV.md
│   └── Lab_9_summary.md
├── package-lock.json
├── package.json
├── private_key.pem
├── public_key.pem
├── totp_qr.marz.png
├── totp_qr.png
└── README.md
```


## Learning Objectives Demonstrated

### Cryptography & Secure Communication (Labs 1–3)

- RSA key generation and management using generate_keys.py.
- Hybrid encryption (RSA + AES) via sender_client.py and server_receiver.py:
    - Public-key encryption to protect the AES session key.
    - Symmetric AES-CFB to encrypt the actual message.
- Message integrity and confidentiality in transit over sockets.
- Password security with:
    - Secure password hashing (hashing.py).
    - Salting and peppering strategies (salt_pepper.py).
    - Password strength checking (password_checker.py).
- Online authentication and 2FA:
    - Basic authentication flow with an authentication_class.
    - Time-based one-time passwords (TOTP) using 2FA.py and the QR code images.

### File & System Integrity, Malware Concepts (Lab 4 & 6)

- File integrity monitoring:
    - Baseline hash creation (file_integrity_baseline.py) using SHA algorithms (SHAalgo.py).
    - Change detection via file_integrity_check.py comparing current vs baseline hashes.
- Simple malware / worm behaviour:
    - Simulated worm scanning logic in Worm_scan.py.
    - Lightweight malware detection ideas in malware_detect.py.
- Network monitoring:
    - Reading and analysing network connection logs in Network_monitor.py using connections.csv.
- Binary analysis & triage (Lab 6):

    - Static hashing of binaries (hash_calc.py, binary_analysis.py) to identify and label samples.
    - String extraction from executables (string_extraction.py) to reveal URLs, paths, and potential IoCs.
    - PE header inspection (pe_header_inspect.py) to understand Windows executable metadata.
    - YARA-style IOC matching (ioc_yara.py) as an introduction to rule based malware detection.

### Web & Network Security, Reconnaissance (Labs 5 & 7)

- Web security testing (web_security.py):
    - Exploring common web vulnerabilities conceptually (e.g. XSS / injection).
    - Input validation and basic sanitisation techniques.
- Port scanning and service enumeration:
    - Custom port scanner (Port_scanner.py) to identify open ports and understand TCP connection behaviour.
    - Use of Nmap.py to integrate / simulate Nmap-style scanning.
- Domain intelligence & WHOIS:
    - Gathering WHOIS data via Whois_domain_lookup.py.
- Penetration testing methodology:
    - Documented workflows and planning in Pen_test.py and Lab_7_summary.md:
        - Scoping and rules of engagement.
        - Reconnaissance, scanning, enumeration.
        - Basic exploitation concepts and reporting.

### AI & LLM Security (Lab 9)

Lab 9 focuses on security in modern AI systems, particularly large language models (LLMs):

- Model behaviour & evaluation:
    - Running and interacting with LLMs in LLM_model.py, gemma3.py, and qwen7b.py.
- Adversarial attack vectors against LLMs:
    - Prompt injection testing (Prompt_injection.py).
    - Model inversion (Model_inversion.py) – attempting to infer sensitive training data.
    - Model extraction (Model_extraction.py) – simulating attempts to clone a model’s functionality.
    - Data poisoning (Data_poinsoning.py) – exploring the impact of malicious data on model outputs.
- Documentation & reflection:
    - LLM_findings.md and Part_IV.md summarise the experiments, risks, and mitigations, linking them back to traditional security principles (CIA triad, access control, least privilege).

## Lab-by-Lab Summary

### Lab 1 – Introduction & Foundations

- Portfolio and module overview (PDF).
- Sets out the baseline expectations for security labs and documentation.
- Forms the starting point for aligning my work with the assessment criteria.

### Lab 2 – RSA, AES & Socket Programming

- Implemented an end-to-end encrypted message exchange using RSA + AES hybrid cryptography.
- Generated RSA key pairs and stored them as PEM files (public_key.pem, private_key.pem).
- Implemented a TCP socket server (server_receiver.py) and client (sender_client.py).
- Demonstrated successful decryption of ciphertext and validated confidentiality.
- See: Lab_2_Summary.md and Peer_Reflection_summary.md.

### Lab 3 – Authentication, Hashing & 2FA

- Explored secure password storage using hashing, salting, and peppering.
- Built a password checker and experimented with brute forcing (Brute_force.py) to understand the importance of strong passwords.
- Implemented a simple multi-step authentication flow (authentication_class.py).
- Added a second factor of authentication using TOTP and QR codes (2FA.py, totp_qr.png, totp_qr_marz.png).
- See: Lab_3_Summary.md.

### Lab 4 – File Integrity, Malware & Network Monitoring

- Created a cryptographic baseline of file hashes and used it to detect tampering.
- Worked with test files in Lab 4/Files/ and monitored changes via CSV outputs.
- Simulated worm behaviour and malware detection to understand how signatures and anomalies are used in practice.
- Analysed simple connection data with Network_monitor.py to spot suspicious traffic.
- See: Lab_4_Summary.md.

### Lab 5 – Web Security

- Implemented basic web-security themed logic in web_security.py.
- Reflected on common vulnerabilities (e.g. XSS, SQLi) and the importance of validation, encoding, and least privilege.
- See: Lab_5_Summary.md.

### Lab 6 – Binary Analysis & YARA-Style Rules

- Performed static analysis of binaries via hashing (hash_calc.py, binary_analysis.py).
- Extracted human-readable strings (string_extraction.py) to uncover potential IoCs.
- Inspected PE headers (pe_header_inspect.py) for metadata such as sections, imports, and compilation details.
- Experimented with IOC/YARA-like rules (ioc_yara.py) to flag suspect executables.
- See: Lab_6_summary.md.

### Lab 7 – Port Scanning, WHOIS & Pen-Test Planning

- Built a simple Python port scanner for localhost and remote hosts (Port_scanner.py).
- Used WHOIS lookups (Whois_domain_lookup.py) to gather domain registration details.
- Incorporated (or simulated) Nmap scanning workflows in Nmap.py.
- Developed a penetration-testing style plan and reflection (Pen_test.py, Lab_7_summary.md), emphasising ethics, scope, and documentation.

### Lab 9 – LLM & Model Security

- Ran experiments with locally hosted LLMs (LLM_model.py, gemma3.py, qwen7b.py).
- Implemented scripts to explore:
    - Prompt injection (Prompt_injection.py)
    - Data poisoning (Data_poinsoning.py)
    - Model inversion (Model_inversion.py)
    - Model extraction (Model_extraction.py)
- Documented findings in LLM_findings.md and Part_IV.md, explicitly connecting them to:
    - Training-data confidentiality.
    - API and access-control design.
    - Risks of deploying LLMs into security-sensitive workflows.
- See: Lab_9_summary.md.

## Evidence of Technical Growth

This portfolio demonstrates:

- Progression from basic to advanced topics
Starting from simple key generation and socket programming, I moved into malware concepts, binary analysis, network recon, and eventually LLM security.
- Hands-on understanding of core security principles
    - Confidentiality, integrity, and availability (CIA triad) in different contexts.
    - Authentication, authorisation, and accountability.
    - Secure configuration and defence-in-depth.
- Debugging & problem-solving

    - Handling socket timeouts and partial reads in Lab 2.
    - Fixing issues with large file handling and memory usage in binary analysis (Lab 6).
    - Interpreting unexpected scan results and WHOIS output in Lab 7.
    - Understanding surprising or unsafe LLM responses in Lab 9 and turning them into learning points.
- Professional documentation
    - Each lab includes structured summaries that:
        - Explain what I implemented.
        - Reflect on what went wrong and how I fixed it.
        - Connect the technical work to real-world security implications.



## Challenges & Solutions

### Socket Issues
Encrypted messages arrived partially; I fixed it by implementing buffered chunk reading.

### Binary Handling
Large file crashes led me to implement safer buffered reading techniques.

### Scan Timeouts
Investigating silent drops helped me understand firewall behaviour and TCP retransmissions.



## Alignment with Assessment Criteria
This portfolio demonstrates:

- Clear, structured documentation  
- Correct and technically sound implementations  
- Analytical reflections  
- Professional presentation  


## Final Statement
This portfolio reflects my progression through applied cybersecurity tasks, growing from foundational experiments to more advanced cryptographic, network, and system-level security work. It demonstrates both technical skill and reflective understanding of core security principles.


# AI declaration


Throughout this module, AI was used for the following: 

Templating, structuring, debugging as well as explaining parts of the lab and lectures. This helped build my understanding of core security priciples during the completion and studying of the module, for the labs and lectures. 
