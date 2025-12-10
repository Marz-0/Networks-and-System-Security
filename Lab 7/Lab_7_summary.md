# Week 7 – Penetration Testing Summary

## 1. Introduction to Penetration Testing
This week focused on the foundations of penetration testing (pen testing). This includes its purpose, methodology, and ethical requirements. Pen testing is a controlled security assessment where an authorised tester or a team of testers attempt to identify vulnerabilities before malicious actors do. The idea behind this is to find vulnerabilities before actual malicious hackers do. 

A key principle covered this week was legality:  
- Pen testing must only be done with explicit permission on systems you own or are authorised to test.
- All activities in this lab were carried out on localhost or public domains for which only passive information was retrieved.



## 2. Penetration Testing Methodology
Penetration testing typically follows these stages:

1. **Reconnaissance** – Gathering information (passive & active).
2. **Scanning / Enumeration** – Identifying open ports, services, and system details.
3. **Vulnerability Assessment** – Matching findings to known weaknesses.
4. **Exploitation** – Attempting to use vulnerabilities to gain access.
5. **Post-Exploitation** – Expanding or maintaining access once inside.
6. **Reporting** – Documenting findings clearly and professionally.

This lab focused mainly on **reconnaissance** and **scanning**.



## 3. Practical Tasks Completed

### Whois Domain Lookup (Passive Reconnaissance)

`Whois_domain_lookup.py`  

This python file/script resolves the IP address of a domain and then attempts to retrieve WHOIS style public information (such as organisation, city, and country) from an API.

Example run:

- Resolved `bbc.co.uk` to `151.101.0.81`
- The API response in this run returned an error, so the script printed:  
  `Could not fetch WHOIS data.`

This still demonstrates:

- Passive reconnaissance using DNS
- Handling failures from external APIs gracefully



### Black Box Reconnaissance (HTTP Header Analysis) 

`Pen_test.py`  

This script performs a **black box** style check by sending an HTTP HEAD request to a website and printing selected response headers:

- `Server`
- `Content-Type`

In my run, the output was:

- `Server: Varnish`
- `Content-Type: Unknown`

This shows how much (or how little) can be learned from server headers, and that some servers or CDNs (Content Delivery Network's) hide or minimise information for security reasons.



### Manual Port Scanner (Socket-Based)

`Port_scanner.py`  

This scanner checks common ports on `127.0.0.1` using Python sockets. It tests a list of ports (e.g. 22, 80, 443, 8080) and records which ones respond as open.

In my environment, the output was:

`Open ports on 127.0.0.1: []`

This means that all of the tested ports were closed at the time of the scan. Even though there were no open ports, the script successfully demonstrates:

- How TCP port checks work
- How scanning tools determine if services are exposed
- How to interpret an empty result as “no tested ports open”



### Nmap Scan with python-nmap (Service Detection)

`Nmap.py`  

Using the `python-nmap` library, this script performs a more advanced Nmap-style scan of `127.0.0.1` over the port range `1-10`, including service detection.

Example output:

- Host `127.0.0.1` was reported as **up**
- Ports 1–10 were reported as **closed**, with known service names where applicable (e.g. `tcpmux`, `compressnet`, `echo`)

This demonstrates:

- Integration of Python with the Nmap tool
- How Nmap reports host state and port states (open/closed)
- How service names are mapped to ports, even when they are closed



## 4. Ethical and Legal Considerations
This week's seminar emphasised:

- **Never test systems without explicit written permission**
- Always use isolated, safe environments such as localhost or VMs
- Follow professional guidelines and legal frameworks
- Ethical hacking must prioritise safety, responsibility, and accountability

My tests were limited to:

- Localhost (`127.0.0.1`) for active scanning  
- Public domains for passive information only



## 5. What I Learned
During Week 7, I gained practical skills relevant to penetration testing:

- How to safely collect public information about a domain and handle API failures
- How server headers can reveal (or intentionally hide) useful information
- How manual scanners detect open ports and how to interpret situations where all tested ports are closed
- How Nmap performs detailed scanning and service mapping, even when ports are closed
- Why reconnaissance and scanning are critical steps before deeper testing

This week strengthened both my technical skills and ethical understanding in cybersecurity and penetration testing/ethical hacking.
