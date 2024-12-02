#!/bin/bash

# Output file for firewall logs
OUTPUT_FILE="$HOME/Software-Programming-final-project/monitor_logs/firewall_logs_output.log"

# Inform the user about the monitoring process
echo "Monitoring iptables logs and logging to: $OUTPUT_FILE"

# Monitor iptables rules and append changes to the output file
while true; do
  echo "Current iptables Rules:" >> "$OUTPUT_FILE"
  iptables -L >> "$OUTPUT_FILE" 2>/dev/null
  echo "-------------------------------" >> "$OUTPUT_FILE"
  sleep 10  
done
