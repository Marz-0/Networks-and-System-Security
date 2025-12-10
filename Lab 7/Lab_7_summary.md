# Week 7

## Penetration Testing Summary

## 1. Introduction to Penetration Testing

This week focused on the foundations of penetration testing (pen testing). including its purpose, methodology, and ethical requirements. Pen testing is a controlled security assessment where authorised testers attempt to identify vulnerabilities before malicious actors do.

A key principle covered this week was legality:
Pen testing must only be done with explicit permission on systems you own or are authorised to test.

## 2. Penetration Testing Methodology

Penetration testing typically follows these stages:

Reconnaissance – Gathering information (passive & active).

Scanning / Enumeration – Identifying open ports, services, and system details.

Vulnerability Assessment – Matching findings to known weaknesses.

Exploitation – Attempting to use vulnerabilities to gain access.

Post-Exploitation – Expanding or maintaining access once inside.

Reporting – Documenting findings clearly and professionally.

This lab focused mainly on reconnaissance and scanning.

## 3. Practical Tasks Completed

### Whois Domain Lookup (Passive Reconnaissance)

Script: Whois_domain_lookup.py
This script resolves a domain's IP address, then retrieves WHOIS-style public information (organisation, city, and country) from a free API.
This demonstrates passive intelligence gathering without directly interacting with the target.

### Black Box Reconnaissance (HTTP Header Analysis)

Script: Pen_test.py
Using an HTTP HEAD request, the script extracts visible server information such as:

Server header

Content-Type

This simulates an early black-box assessment where no internal system knowledge is available.

### Manual Port Scanner (Socket-Based)

Script: Port_scanner.py
This scanner checks common ports on 127.0.0.1 using Python sockets. It demonstrates:

How TCP port checks work

How scanning tools determine if services are exposed

Why port enumeration is crucial before further testing

### Nmap Scan with python-nmap (Service Detection)

Script: Nmap.py
Using the python-nmap library, this script performs real Nmap-style scanning:

Port scanning

Service/version detection (-sV)

Host discovery

This provides deeper insights into running services and potential vulnerabilities.

4. Ethical and Legal Considerations

This week's seminar emphasised:

- Never test systems without explicit written permission
- Always use isolated, safe environments such as localhost or VMs
- Follow professional guidelines and legal frameworks
- Ethical hacking must prioritise safety, responsibility, and accountability

5. What I Learned

During Week 7, I gained practical skills relevant to penetration testing:

- How to safely collect public information about a domain
- How server headers can reveal valuable information
- How manual scanners detect open ports
- How Nmap performs detailed service enumeration
- Why reconnaissance and scanning are critical steps before deeper testing

This week strengthened both my technical skills and ethical understanding in cybersecurity.