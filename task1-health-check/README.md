# Task 1: Health Check Automation

## Objective
Automate basic system and application health checks to verify availability and responsiveness.

---

## Description
This task implements a Python-based health check script that validates the availability of defined endpoints or services.  
The script captures response status and response time, then logs the results for monitoring and review.

This simulates real-world application health monitoring used in IT operations and DevOps environments.

---

## Files
- `health_check.py` – Main script to perform health checks
- `health_check.log` – Generated log file with health status

---

## How It Works
1. Reads a list of URLs to check
2. Sends HTTP requests to each endpoint
3. Captures:
   - HTTP status
   - Response time
4. Logs the results in a structured format

---

## How to Run
```bash
python health_check.py
```

## Skills Demonstrated

- Python scripting

- HTTP requests

- Logging

- Basic monitoring automation
