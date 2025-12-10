# Week 05 Practical Summary  
**Web Security & Vulnerability Scanning with Wapiti**

In this lab I explored **web application vulnerability scanning** using the Wapiti tool. Wapiti performs black-box testing against a web application by crawling pages and injecting payloads to test for issues such as cross-site scripting (XSS), SQL injection, command injection, file inclusion, insecure file uploads, and SSRF. This fits into a typical web security audit workflow, where automated scans are used to quickly highlight potential weaknesses before they are manually verified.  

Before running any scans, we were reminded of the importance of **ethical hacking**: vulnerability scanning must only be carried out against applications where we have explicit permission. For this exercise I focused on deliberately vulnerable training applications such as **Google Gruyere** or **OWASP Juice Shop**, which are designed to be safely attacked for learning purposes. These platforms contain many common issues (XSS, SQLi, insecure direct object references, etc.), making them ideal for understanding how scanners behave.

I then installed Wapiti (via `pip install wapiti3`) and used the command-line interface to run a scan against my chosen target. The scanner was executed with a command similar to:

wapiti -u <TARGET_URL> -o juice_wapiti_report -f html



This tells Wapiti which URL to test, where to store the results, and that the output should be in HTML format. To make this process easier and more reproducible, I wrote a Python script called web_security.py that (1) prompts for a target URL, (2) runs the Wapiti scan, and (3) locates the resulting HTML report. The script includes a helper function that searches for the newest .html report file and, when running in a notebook, renders it inline; otherwise it prints the report path so it can be opened in a browser.

After the scan completed, I opened the Wapiti report to review the findings. The report groups results by vulnerability type and affected URL or parameter. For example, it can show possible reflected XSS where user input is echoed back into the page without proper escaping, or potential SQL injection points where parameters appear to affect database queries. Not every item is guaranteed to be exploitable (there can be false positives), but each one represents a starting point for manual verification. This process helped me see how automated tools prioritise issues and how they present evidence such as payloads, HTTP requests, and responses.

Overall, this lab reinforced several key ideas about web security. Firstly, automation is powerful but not sufficient on its own: a scanner can quickly highlight suspicious inputs and endpoints, but human analysis is still needed to confirm and safely exploit or remediate vulnerabilities. Secondly, the variety of findings showed how many different attack surfaces a typical web app exposes—URLs, forms, headers, uploads, and back-end services. Finally, the emphasis on permissions and safe targets underlined the legal and ethical responsibilities of security testing. This lab gave me practical experience running a professional-style web vulnerability scan and interpreting the results in the context of real-world web application security.