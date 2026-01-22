from datetime import datetime

#File Paths
INPUT_FILE = "sample_input.log"
OUTPUT_FILE = "output_report.txt"

#Initialize counters
info_count = 0
warning_count = 0
error_count = 0

#Read the log file
with open(INPUT_FILE, "r") as file:
    for line in file:
        if "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "ERROR" in line:
            error_count += 1

# Generate timestamp
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create report content
report_content = f"""
AUTOMATED LOG SUMMARY REPORT
Generated on: {current_time}

Summary:
INFO messages : {info_count}
WARNING messages : {warning_count}
ERROR messages : {error_count}

End of Report
"""

# Write report to output file
with open(OUTPUT_FILE, "w") as report_file:
    report_file.write(report_content)
print("Report genreated successfully.")        