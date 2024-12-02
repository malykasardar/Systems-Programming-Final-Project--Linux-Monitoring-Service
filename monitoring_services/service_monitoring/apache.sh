#!/bin/bash

# Get the absolute path of the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="$SCRIPT_DIR/../../monitor_logs/service_logs"
LOG_FILE="$LOG_DIR/apache_service.log"

# Create the log directory if it doesn't exist
mkdir -p "$LOG_DIR"

# Write log information to the log file
echo "Monitoring Apache Service..." > "$LOG_FILE"

# Check if Apache is running
if pgrep apache2 > /dev/null 2>&1; then
    echo "$(date): Apache is running." >> "$LOG_FILE"
else
    echo "$(date): Apache is NOT running." >> "$LOG_FILE"
fi

echo "Log updated at $(date)" >> "$LOG_FILE"

# Flush everything to disk
sync

echo "apache done"
