#!/bin/bash

# Base Discord directory
DISCORD_DIR="$HOME/Library/Application Support/discord"

# Discord log file
LOG_FILE="modules.log"

# Verify that the log file exists
if [ ! -f "$DISCORD_DIR/$LOG_FILE" ]; then
  echo "Log file not found: $DISCORD_DIR/$LOG_FILE"
  exit 1
fi

# Store logs in a temporary file
OUTPUT_FILE="$HOME/Software-Programming-final-project/monitor_logs/discord_logs_output.log"

echo "Monitoring Discord logs at: $DISCORD_DIR/$LOG_FILE"
echo "Writing log output to: $OUTPUT_FILE"

# Define a pattern to track (e.g., warnings)
PATTERN="warning"

# Monitor log file and track patterns
tail -F "$DISCORD_DIR/$LOG_FILE" | while read -r line; do
  if echo "$line" | grep -i "$PATTERN" >/dev/null; then
    # If the pattern is found, output the log entry and "true"
    echo "{ $line } true" | tee -a "$OUTPUT_FILE"
  else
    # If there's no match, output "false"
    echo "false" | tee -a "$OUTPUT_FILE"
  fi
done
