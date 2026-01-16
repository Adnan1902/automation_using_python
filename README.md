# Task 1: Automated Health Check Script

## Overview
This project implements an automated health check script using Python.  
The script periodically checks the availability of applications or servers by sending HTTP requests and logging their status.

It identifies whether a service is:
- **UP** (HTTP 200)
- **DOWN** (Non-200 response like 500)
- **ERROR** (Timeouts, connection issues, exceptions)

All results are logged with timestamps and response times.

---

## Features
- HTTP health check using real URLs
- Measures response time
- Handles server errors and network exceptions
- Logs results to a file
- Clean Git version control with ignored log files

---

## Technologies Used
- Python 3
- `requests` library
- Python `logging` module
- Git & GitHub

---

## Project Structure
task1-health-check/
│
├── health_check.py      # Main health check script
├── README.md            # Documentation
└── .gitignore           # Ignores log files

---

## How It Works
1. A list of URLs is defined in the script
2. Each URL is checked using an HTTP GET request
3. Response time is calculated
4. Status is classified as UP / DOWN / ERROR
5. Results are logged with timestamps

---

## Sample URLs Used
- https://www.google.com (Expected UP)
- https://www.github.com (Expected UP)
- https://httpbin.org/status/500 (Simulated server error)
- https://10.255.255.1 (Simulated timeout)

---

## How to Run
### Prerequisites
- Python 3 installed
- `requests` library installed

Run the script

python health_check.py

Logs will be generated automatically.


Learning Outcomes
	•	Basic automation scripting
	•	HTTP monitoring logic
	•	Exception handling
	•	Logging best practices
