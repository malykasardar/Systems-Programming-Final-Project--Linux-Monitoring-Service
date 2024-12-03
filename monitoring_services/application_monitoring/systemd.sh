#!/bin/bash

# Output file for system logs
OUTPUT_FILE="$HOME/Software-Programming-final-project/monitor_logs/application_logs/sys_utils"

# Notification of the monitoring process
echo "Monitoring system logs (systemd) and logging to: $OUTPUT_FILE"

# Monitor system logs and append new entries to the output file
log stream | while read -r line; do
  echo "$line" | tee -a "$OUTPUT_FILE"
done
