#!/bin/bash

# Output file to save logs
OUTPUT_FILE="$HOME/Software-Programming-final-project/monitor_logs/command_logs_output.log"

# Notification of the monitoring process
echo "Saving command outputs to: $OUTPUT_FILE"

# Save the output in a file (eg: `df -h` for disk usage)
while true; do
  echo "Running command 'df -h' to display disk usage: " | tee -a "$OUTPUT_FILE"
  df -h | tee -a "$OUTPUT_FILE"
  echo "-------------------------------" | tee -a "$OUTPUT_FILE"
  sleep 60 
done
