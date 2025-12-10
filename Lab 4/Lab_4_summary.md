# Week 4 Practical Summary  


## Malware, Integrity & Network Monitoring

In this week’s practical, I explored core defensive techniques used to detect and analyse malicious software. I first implemented a simple File Integrity Monitoring (FIM) system. 

The first script generated a SHA-256 hash for every file in a monitored directory ("Files" folder) and saved the results into a baseline.csv file. This establishes a trusted reference point. The script file_integrity_baseline.py walks through the folder. It hashes each file and records its timestamp, simulating how host based intrusion detection systems create clean system baselines.

After generating the baseline, I used file_integrity_check.py to detect suspicious changes. The script recomputes each file’s hash and compares it to the baseline to identify new, modified, or missing files. This demonstrates how integrity checking can reveal tampering caused by malware.

Next, I implemented a simple signature-based malware scanner. The script malware_detect.py (signature_scan) scans files for known malicious patterns such as eval or socket.connect, representing static detection techniques. This acts like an antivirus feature. Any matching pattern produces a warning, showing how signature rules can help identify suspicious scripts.

To understand malware propagation, I created a worm simulation using Worm_scan.py. This script randomly selects hosts and attempts to infect them with a set probability, printing the spread at each step. It then models how scanning worms propagate across a network, and how infection speed depends on factors like probability and the number of hosts contacted.

Finally, I developed a basic network monitoring tool using Network_monitor.py. This program analyses a CSV log of outbound connections and raises alerts if any device exceeds a certain number of connections. This could indicate worm like behaviour or scanning activity. This shows how network level anomaly detection can complement host based monitoring by looking for unusual communication patterns.

Overall, this practical strengthened my understanding of malware behaviour and defensive techniques. I gained hands on experience with integrity checking, signature detection, simulated malware propagation, and basic network anomaly monitoring core elements of modern cybersecurity defence strategies.