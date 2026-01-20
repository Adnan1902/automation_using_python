# Task 2: Automated Log Error Detection

## Overview
This project automatically scans application log files to detect error patterns such as **ERROR**, **FAILED**, and **EXCEPTION**.  
It helps identify issues early without manually checking large log files.

---

## Why This Automation?
- Logs grow very large over time
- Manual scanning is slow and error-prone
- Automated detection ensures faster incident awareness
- Useful in DevOps, SRE, and production monitoring

---

## Features
- Scans log files line by line
- Detects predefined error keywords
- Counts total error occurrences
- Triggers an alert if error count crosses a threshold
- Logs detected errors using Python logging

---

## Technologies Used
- Python 3
- File handling
- Pattern matching
- Logging module

---

## Project Structure
# Task 2: Automated Log Error Detection

## Overview
This project automatically scans application log files to detect error patterns such as **ERROR**, **FAILED**, and **EXCEPTION**.  
It helps identify issues early without manually checking large log files.

---

## Why This Automation?
- Logs grow very large over time
- Manual scanning is slow and error-prone
- Automated detection ensures faster incident awareness
- Useful in DevOps, SRE, and production monitoring

---

## Features
- Scans log files line by line
- Detects predefined error keywords
- Counts total error occurrences
- Triggers an alert if error count crosses a threshold
- Logs detected errors using Python logging

---

## Technologies Used
- Python 3
- File handling
- Pattern matching
- Logging module

---

## Project Structure
task2-log-analyzer/
│── log_analyzer.py
│── sample_app.log
│── README.md
│── .gitignore

---

## How It Works
1. Reads the log file (`sample_app.log`)
2. Searches for keywords:
   - ERROR
   - FAILED
   - EXCEPTION
3. Counts matching log entries
4. Prints total error count
5. Raises an alert if threshold is exceeded

---

## How to Run

```bash
python log_analyzer.py
```
Sample Output
Total error entries found: 3
ALERT: Error threshold exceeded!

#Automation Skills Demonstrated: 
	•	File handling
	•	Pattern matching
	•	Conditional logic
	•	Basic alerting
	•	Log analysis

