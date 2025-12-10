# Week 6 Practical Summary 

## Binary Analysis & Symbolic Execution

In this week's lab, I carried out a full static analysis on a Windows executable (`Procmon.exe` from Microsoft
Sysinternals). The aim is to understand how malware analysts triage
suspicious files by using safe and non executing techniques. This includes:

-   Computing cryptographic hashes 
-   Extracting readable strings, 
-   Inspecting PE headers 
-   Identifying potential Indicators of Compromise (IOCs), 
-   Applying a basic YARA rule for pattern matching.

## 1. Cryptographic Hash Calculation

I first started by generating three different cryptographic hashes of the
executable: **MD5**, **SHA1**, and **SHA256** 
These hashes act as unique fingerprints and are usually used as
Indicators of Compromise (IOCs) for the following:

-   Threat intelligence reports
-   SOC alert correlation
-   File deduplication
-   Detecting tampered or modified binaries

Even a one-byte change in the file would completely alter all three
hashes due to the avalanche effect.

## 2. String Extraction

Afterwards, I extracted text strings from the binary by
scanning for ASCII sequences of four or more characters.
This step often reveals early hints about malware behaviour. 
For example:

-   File system paths
-   Registry keys
-   Command and Control URLs
-   Hardcoded credentials
-   Error messages

For the benign `Procmon.exe` sample, the strings mainly consisted of:

-   DLL names
-   Menu labels
-   System messages
-   Internal application strings

## 3. PE Header Inspection

Using the `pefile` library, I inspected the structure of the Windows
Portable Executable (PE) format.
I extracted key fields such as:

-   **Entry Point:** where execution begins
-   **Image Base:** the preferred memory loading address
-   **Imported DLLs and functions:** shows all Windows APIs the program
    relies on

Procmon imports libraries such as `kernel32.dll`,
`user32.dll`, and `advapi32.dll`.
In malware, unusual or suspicious API usage like `CreateRemoteThread`,
`VirtualAllocEx`, or `LoadLibraryA` may indicate process injection or
shellcode loading.

## 4. IOC Extraction (URLs & IPs)

I performed a simple pattern search on the decoded binary content to
identify possible:

-   URLs
-   IPv4 addresses

This is a common triage step for detecting Command and Control servers
or malicious infrastructure.
Procmon did not contain harmful indicators, highlighting
its benign nature.

## 5. YARA Rule Matching

Finally, I wrote and executed a simple YARA rule that triggers whenever
the string `"http"` appears within the file.

This demonstrated how YARA rules are used in:

-   SOC pipelines
-   Malware classification
-   Signature-based detection
-   Large scale automated file scanning

The rule matched cases of `"http"` found in Procmon's
embedded strings.

## Conclusion

By completing all tasks, I gained practical experience in static malware
triage techniques, including:

-   Hash generation
-   String extraction
-   PE file inspection
-   IOC discovery
-   Basic YARA rule usage

Although the sample used was benign, this Weeks lab shows how early
stages of real world malware analysis is like and helps build essential skills
for threat investigation, incident response, and security engineering.
