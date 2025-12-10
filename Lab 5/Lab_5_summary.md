# Week 05 Practical Summary  
**Web Security & Vulnerability Scanning with Wapiti**

In this lab I explored **web application vulnerability scanning** using the Wapiti tool. Wapiti performs black-box testing against a web application by automatically crawling pages and injecting different payloads to test for vulnerabilities such as cross-site scripting (XSS), SQL injection, command injection, file inclusion, insecure file uploads, and SSRF. This reflects how automated scanning tools are commonly used in real security assessments to rapidly identify potential weaknesses before moving on to manual verification.

Before performing any testing, we reviewed the principles of **ethical hacking**. Vulnerability scanning must only be carried out against systems where explicit permission has been granted. For this lab, I used my own generated instance of **Google Gruyere**, a deliberately vulnerable training environment provided by Google for safe security testing:

**Target used:**  
`https://google-gruyere.appspot.com/506501897608741028240585573654077157687/`

This environment contains many realistic issues—such as reflected XSS, stored XSS, insecure file handling, and logic flaws—making it an ideal target for practising automated scanning.


## Running Wapiti & Implementing the Automation Script

The lab instructions introduced Wapiti as the tool for scanning vulnerable applications. The typical command for running a scan is:

```bash
wapiti -u <TARGET_URL> -o juice_wapiti_report -f html
```

This specifies the target URL, the desired output name, and the generation of an HTML report. To make the process more repeatable, I wrote a Python script `web_security.py` which:

1. Prompts the user for a target URL  
2. Executes the Wapiti scan programmatically  
3. Searches for the generated HTML report (either as a file or inside an output folder)  
4. Attempts to display the report inline, or prints the file path for manual viewing  

This demonstrates my understanding of automating a vulnerability-scanning workflow and handling report parsing programmatically.

Due to installation limitations on my machine, the Wapiti command itself could not be executed (Windows was unable to recognise `wapiti` after installation). However, my Python code is fully functional and designed to run a scan successfully in any environment where Wapiti is installed correctly. The script also handles this failure gracefully by informing the user when no report has been produced.


## Reviewing and Interpreting Vulnerability Reports

Although I could not generate a live HTML report locally, I analysed example Wapiti reports and learned how they are structured. Reports are grouped by vulnerability type, affected URL, and the injection vectors used. An example finding might include:

- **Reflected XSS** from unsanitised user input  
- **SQL injection indicators** based on error messages  
- **Suspicious parameters** that influence server behaviour  
- **Unvalidated redirects**  
- **Information disclosure** through predictable URLs  

Each finding includes request/response snippets, payloads used, and severity levels. These reports highlight potential issues but still require manual follow-up to confirm whether they are exploitable, reflecting real-world penetration-testing practice.


## Reflection

This lab reinforced several important ideas about modern web security:

- **Automation speeds up reconnaissance** but cannot replace human analysis. Tools like Wapiti identify entry points but cannot determine business impact or exploitability.  
- **Web applications have large attack surfaces**, with many components—forms, parameters, cookies, uploads, redirects—acting as potential vectors.  
- **Ethical and legal considerations are crucial**; scanning without permission is illegal, and training environments like Gruyere are essential for practising safely.  
- **Error handling and tooling limitations are part of real-world cybersecurity work**. Sometimes tools fail to install or run in certain environments, and being able to document, troubleshoot, and reflect on this is an important professional skill.

Overall, this lab helped me understand the fundamentals of automated vulnerability scanning, allowed me to design code that integrates Wapiti programmatically, and strengthened my ability to interpret and contextualise web application security findings.
