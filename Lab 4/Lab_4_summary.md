# Week 4 Practical Summary  
## Malware, Integrity Monitoring & Network Anomaly Detection

In this practical session, I implemented a set of defensive security tools designed to simulate how real-world systems detect, analyse, and respond to malicious software. The workshop focussed on four core areas: file integrity monitoring, signature-based malware detection, worm propagation modelling, and network anomaly detection. Together, these exercises provided a hands-on understanding of how security mechanisms identify unusual behaviour and protect systems from compromise.



## 1. File Integrity Monitoring (FIM)

The first task involved creating a **baseline of trusted file hashes**. Using SHA‑256, I generated a cryptographic fingerprint for every file inside the monitored *Files/* directory.  
The script `file_integrity_baseline.py` walks through each file, hashes it, and records the results in **baseline.csv**, including timestamps for traceability. This mirrors how host‑based intrusion detection systems maintain a database of “clean” system states.

Next, I used `file_integrity_check.py` to compare the current state of the folder with the baseline. The script re‑hashes all files and identifies whether each one is:

- **[OK]** – unchanged  
- **[MODIFIED]** – hash mismatch  
- **[NEW]** – not present in the baseline  
- **[MISSING]** – removed since the baseline  

This demonstrates how integrity monitoring can detect unauthorised modification—one of the key behavioural signs of malware attempting to tamper with files or embed itself into a system.



## 2. Signature‑Based Malware Scanning

To explore classic antivirus techniques, I built a simple signature scanner using `signature_scan.py`.  
The program:

- Reads every file in the monitored directory  
- Searches for suspicious patterns such as:
  - `eval(`  
  - `base64.b64decode`  
  - `socket.connect`  
  - `exec(`  
  - `import os`  
- Flags any file that contains these indicators

Although signature‑based detection is limited—especially against polymorphic or obfuscated malware—it remains useful for identifying basic malicious behaviours. This exercise shows how early antivirus engines worked and why modern systems rely on more sophisticated behavioural analysis.

### 2.5 How to use malware detect:

to test the signature-based malware scanner:

Place a file inside the Files/ directory (this is the folder the scanner checks).

You can call this file:

test_malware.py

Add content that contains one of the suspicious patterns into this file, for example:

```bash 
# test file
import os
eval("print('malicious')")
```

Run the scanner:

python signature_scan.py


If the scanner finds a matching signature, it prints a warning like:

[SUSPICIOUS] Files/test.py matches pattern: eval(


This demonstrates how signature-based antivirus tools detect known malicious patterns in files.





## 3. Worm Propagation Simulation

Using `worm_scan.py`, I modelled how a network worm spreads across a set of simulated hosts.  
The script:

- Starts with a single infected host  
- Makes several infection attempts per step  
- Infects new hosts based on probability  
- Displays the infection curve across iterations  

This reflects how scanning worms (like Code Red or SQL Slammer) spread rapidly by randomly probing hosts for vulnerabilities. By adjusting variables such as infection probability or number of attempts, I was able to see how small changes dramatically influence outbreak severity.



## 4. Network Monitoring & Anomaly Detection

To complement host‑based defences, I implemented a lightweight network monitoring tool in `Network_monitor.py`.  
This program:

- Reads **connections.csv**, a log of outbound connections  
- Counts the number of connections per source IP  
- Raises an alert if any device exceeds a defined threshold  

Excessive outbound connections can signal worm activity, port scanning, or command‑and‑control beaconing. This exercise highlights how network‑level anomaly detection can reveal malicious behaviour that file-based monitoring alone might miss.



## Reflection

This practical consolidated key defensive strategies used in cybersecurity:

- **Integrity checking** revealed how cryptographic baselines detect tampering.  
- **Signature scanning** illustrated the foundations (and limitations) of classic antivirus design.  
- **Worm simulation** provided insight into malware propagation and why rapid detection is critical.  
- **Network anomaly detection** demonstrated how unusual connection patterns can indicate an attack in progress.

Together, these tasks gave me a deeper understanding of how malware behaves and how layered detection mechanisms—host-based, network-based, and signature-based—work together to protect systems.

