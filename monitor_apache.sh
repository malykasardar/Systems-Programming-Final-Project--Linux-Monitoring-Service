#!/bin/bash

LOG_DIR="/workspace/monitoring_logs"
LOG_FILE="$LOG_DIR/apache_service.log"

# Ensure log directory exists
mkdir -p "$LOG_DIR"

echo "Monitoring Apache Service..." > "$LOG_FILE"

# Check if Apache is running
if pgrep apache2 > /dev/null 2>&1; then
    echo "$(date): Apache is running." >> "$LOG_FILE"
else
    echo "$(date): Apache is NOT running." >> "$LOG_FILE"
fi

# List active Apache processes
echo "Active Apache Processes:" >> "$LOG_FILE"
ps aux | grep '[a]pache2' >> "$LOG_FILE"

# Track resource usage
echo "Apache Resource Usage:" >> "$LOG_FILE"
top -b -n 1 | grep apache2 >> "$LOG_FILE"

echo "Log updated at $(date)" >> "$LOG_FILE"
