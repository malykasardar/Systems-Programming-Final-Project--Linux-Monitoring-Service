#!/bin/bash

# Base Chrome directory
CHROME_DIR="$HOME/Library/Application Support/Google/Chrome"

# Path to Google Chrome logs and log file
LOG_DIR="$HOME/Library/Application Support/Google/Chrome"
LOG_FILE="chrome_debug.log"

# Verify that the log file exists
if [ ! -f "$LOG_DIR/$LOG_FILE" ]; then
  echo "Log file not found: $LOG_DIR/$LOG_FILE"
  exit 1
fi

# Store logs in a temporary file
OUTPUT_FILE="$HOME/Software-Programming-final-project/monitoring_services/monitor_applications/chrome_logs_output.log"

echo "Monitoring Google Chrome logs at: $LOG_DIR/$LOG_FILE"
echo "Writing log output to: $OUTPUT_FILE"

# Define a pattern to track (e.g., errors)
PATTERN="error"

# Monitor log file and track patterns
tail -F "$LOG_DIR/$LOG_FILE" | while read -r line; do
  if echo "$line" | grep -i "$PATTERN" >/dev/null; then
    # If the pattern is found, output the log entry and "true"
    echo "{ $line } true" | tee -a "$OUTPUT_FILE"
  else
    # If there's no match, output "false"
    echo "false" | tee -a "$OUTPUT_FILE"
  fi
done
