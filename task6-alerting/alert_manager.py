'''
Task 6: Alerting System
Reads a summary report, detects critical error conditions,
and generates timestamped alerts when thresholds are exceeded.
'''

from datetime import datetime

ERROR_THRESHOLD = 3
report_file = "sample_report.txt"
alert_log = "alerts.log"

error_count = 0

# Read the report file
with open(report_file, "r") as file:
    for line in file:
        if "ERROR" in line or "CRITICAL" in line:
            error_count += 1

# Check if alert condition is met
if error_count >= ERROR_THRESHOLD:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert_message = (
        f"[{timestamp}] ALERT: {error_count} critical errors detected\n"
    )

    with open(alert_log, "a") as log:
        log.write(alert_message)

    print("!! Alert generated! !!")
else:
    print("!! System Stable. No alert needed. !!")