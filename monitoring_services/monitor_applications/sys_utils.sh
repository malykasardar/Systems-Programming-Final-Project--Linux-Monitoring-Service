#!/bin/bash

LOG_FILE="sys_utils.log"

# Redirect all output to the log file
exec > >(tee -a "$LOG_FILE") 2>&1

echo "Starting monitoring script..." | tee -a "$LOG_FILE"

# Monitor system processes
echo "Checking system processes related to bash, sysvinit-utils, lsof, and procps..."
ps aux | grep -E "bash|sysvinit|lsof|procps" | grep -v grep | grep -v "$(basename "$0")"

# Monitor application logs
SYSLOG_FILE="/var/log/syslog"
PATTERNS="bash:|error|init:|lsof:|procps:"
echo "Monitoring $SYSLOG_FILE for patterns: $PATTERNS"
tail -F "$SYSLOG_FILE" | grep -E "$PATTERNS" | while read -r line; do
    echo "Log Match: $line"
done &

# Monitor open files using lsof
echo "Tracking open files using lsof..."
lsof | grep -E "bash|sysvinit|lsof|procps"

# Monitor network connections using ss
echo "Tracking network connections..."
ss -tuln

# Infinite loop for continuous monitoring (adjust sleep as necessary)
while true; do
    sleep 60
    echo "Rechecking system processes..."
    ps aux | grep -E "bash|sysvinit|lsof|procps" | grep -v grep | grep -v "$(basename "$0")"
done

