# Task 4: Automation Scheduling (Windows Task Scheduler)

## Overview
This task demonstrates how an automation script can be scheduled to run automatically on a Windows system using Windows Task Scheduler.

The scheduled automation removes the need for manual execution and simulates real-world operational workflows.

---

## Script Scheduled
- Script Name: log_analyzer.py
- Location: task2-log-analyzer/
- Purpose: Analyze application logs and detect error patterns such as ERROR, FAILED, and EXCEPTION.

---

## Scheduler Configuration
- Scheduler Tool: Windows Task Scheduler
- Trigger Type: Daily
- Execution Time: 3:00 PM
- Action: Start a Program

---

## Execution Details
- Program/Script: python.exe (or py.exe)
- Arguments: Full path to log_analyzer.py
- Start In: task2-log-analyzer directory

---
## Outcome
- The log analyzer runs automatically at the scheduled time.
- Errors are detected without manual intervention.
- This setup aligns with production monitoring and alerting workflows.

---

## Notes
- The schedule can be adjusted to hourly or multiple triggers if required.
- Additional alerting mechanics (email, messaging) can be integrated.
