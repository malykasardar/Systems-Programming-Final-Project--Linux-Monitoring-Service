#!/bin/bash
cd ..
cd ..
LOG_DIR="monitor_logs/service_logs"
LOG_FILE="$LOG_DIR/nginx_service.log"

# Ensure log directory exists
mkdir -p "$LOG_DIR"

echo "Monitoring Nginx Service..." > "$LOG_FILE"

# Check if Nginx is running
if pgrep nginx > /dev/null 2>&1; then
    echo "$(date): Nginx is running." >> "$LOG_FILE"
else
    echo "$(date): Nginx is NOT running." >> "$LOG_FILE"
fi

# List active Nginx processes
echo "Active Nginx Processes:" >> "$LOG_FILE"
ps aux | grep '[n]ginx' >> "$LOG_FILE"

# Track resource usage
echo "Nginx Resource Usage:" >> "$LOG_FILE"
top -b -n 1 | grep nginx >> "$LOG_FILE"

echo "Log updated at $(date)" >> "$LOG_FILE"
