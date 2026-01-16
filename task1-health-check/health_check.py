#importing necessary modules
import requests 
import logging 
from datetime import datetime

# Logging Information
logging.basicConfig(
    filename = "health_check.log",
    level = logging.INFO,
    format = "%(asctime)s - @(levelname)s - %(message)s"
)

# Configuration 
URLS = [    
    "https://www.google.com",   # Expected to be UP
    "https://www.github.com",   # Expected to be UP
    "https://httpbin.org/status/500",  # Simulated server Error
    "https://10.255.255.1"  # Simulated timeout/unreachable
]

TIMEOUT = 5  # 5 seconds delay



# Health Check Function

def check_service(url):
    try:
        response = requests.get(url, timeout = TIMEOUT)
        return response.status_code, response.elapsed.total_seconds()
    except Exception as e:
        return None, str(e)

# Main Execution Logic
def main():
    for url in URLS:
        status, info = check_service(url)

        if status == 200:
            logging.info(f"INFO - UP | {url} | response_time={info}s")

        elif status:
            logging .warning(f"INFO| {url} | response_time={info}s | status_code = {status}")
        else:
            logging.error(f"INFO - ERROR | {url} | exception={info}")

# Entry Point
if __name__ == "__main__":
    main()


