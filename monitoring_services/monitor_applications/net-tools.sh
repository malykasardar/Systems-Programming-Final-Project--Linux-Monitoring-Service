#!/bin/bash

# Output file for network monitoring logs
OUTPUT_FILE="$HOME/Software-Programming-final-project/monitor_logs/network_logs_output.log"

# Notification of the monitoring process
echo "Monitoring network logs with net-tools and logging to: $OUTPUT_FILE"

# Monitor active network connections and append to the output file
while true; do
  echo "Current Network Connections:" >> "$OUTPUT_FILE"
  netstat -tuln >> "$OUTPUT_FILE" 2>/dev/null
  echo "-------------------------------" >> "$OUTPUT_FILE"
  sleep 10 
done
