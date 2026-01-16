# Automated Log Error Detection Script

import logging

LOG_FILE = "sample_app.log"
KEYWORDS = ["ERROR", "FAILED", "EXCEPTION"]
ERROR_THRESHOLD = 2

#Configure logging
logging.basicConfig(
    filename = "log_analyzer.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def analyze_logs():
    error_count = 0

    with open(LOG_FILE, "r") as  file:
        for line in file:
            for keyword in KEYWORDS:
                if keyword in line:
                    error_count += 1
                    logging.error(f"Detected {keyword}: {line.strip()}")
    print(f"Total error entries found: {error_count}")

    if error_count >= ERROR_THRESHOLD:
        print("ALERT: Error threshold exceeded!")
        logging.warning("Error threshold exceeded")

if __name__ == "__main__":
    analyze_logs()