#!/bin/bash

LOG_DIR="/workspace/monitoring_logs"
LOG_FILE="$LOG_DIR/mysql_service.log"

# Ensure log directory exists
mkdir -p "$LOG_DIR"

echo "Monitoring MySQL Service..." > "$LOG_FILE"

# Check if MySQL is running
if pgrep mysqld > /dev/null 2>&1; then
    echo "$(date): MySQL is running." >> "$LOG_FILE"
else
    echo "$(date): MySQL is NOT running." >> "$LOG_FILE"
fi

# List active MySQL processes
echo "Active MySQL Processes:" >> "$LOG_FILE"
ps aux | grep '[m]ysqld' >> "$LOG_FILE"

# Track resource usage
echo "MySQL Resource Usage:" >> "$LOG_FILE"
top -b -n 1 | grep mysqld >> "$LOG_FILE"

echo "Log updated at $(date)" >> "$LOG_FILE"
