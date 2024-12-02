#!/bin/bash

# Create a logs directory if it doesn't exist
cd ..
mkdir -p monitor_logs

# Define the log file
LOG_FILE="monitor_logs/resource_monitoring.log"

# Clear the log file if it exists
> "$LOG_FILE"

# Collect CPU usage
echo "=== CPU Usage ===" >> "$LOG_FILE"
top -l 1 | grep "CPU usage" | awk '{print "CPU Usage: " $3 $4}' >> "$LOG_FILE"
echo -e "" >> "$LOG_FILE"

# Collect memory usage (macOS doesn't have 'free', using 'vm_stat')
echo "=== Memory Usage ===" >> "$LOG_FILE"
vm_stat | grep "Pages free" | awk '{print "Free Memory: " $3/256 "MB"}' >> "$LOG_FILE"
# For total and used memory, you can use 'top' as well
top -l 1 | grep "PhysMem" | awk '{print "Total Memory: " $2 ", Used: " $4}' >> "$LOG_FILE"
echo -e "" >> "$LOG_FILE"

# Collect disk usage
echo "=== Disk Usage ===" >> "$LOG_FILE"
df -h | awk '$NF=="/"{printf "Total: %s, Used: %s\n", $2, $3}' >> "$LOG_FILE"
echo -e "" >> "$LOG_FILE"

# Collect network interface info (macOS uses 'ifconfig' instead of 'ip')
echo "=== Network Interfaces ===" >> "$LOG_FILE"
ifconfig | grep inet >> "$LOG_FILE"
echo -e "" >> "$LOG_FILE"

# Collect process information (using 'ps' command without --sort)
echo "=== Running Processes ===" >> "$LOG_FILE"
ps -e -o pid,comm,%mem | head -n 10 >> "$LOG_FILE"
echo -e "" >> "$LOG_FILE"

# Collect open files
echo -e "=== Open Files ===" >> "$LOG_FILE"
lsof | wc -l | awk '{print "Open Files Count: " $1}' >> "$LOG_FILE"

echo "Data collection completed."
