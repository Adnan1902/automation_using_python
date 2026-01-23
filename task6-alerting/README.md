# Task 6: Alerting System

## Objective
Trigger alerts when defined error thresholds are exceeded in reports.

---

## Description
This task reads a generated report file and detects `ERROR` and `CRITICAL` messages.  
If the count crosses a defined threshold, an alert is generated and logged with a timestamp.

This mimics real-world alerting systems used in monitoring and SRE workflows.

---

## Files
- `alert_manager.py` – Alerting script
- `sample_report.txt` – Input report
- `alerts.log` – Generated alert log

---

## How It Works
1. Reads the report file
2. Counts critical error occurrences
3. Compares count with threshold
4. Logs alert with timestamp if threshold is exceeded

---

## How to Run
```bash
python alert_manager.py
```

## Skills Demonstrated

- Threshold-based alerting

- Monitoring automation

- Defensive scripting
