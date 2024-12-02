#!/bin/bash

# Define the log file
LOG_FILE="monitor_logs/resource_monitoring.log"

# Clear the log file if it exists
> "$LOG_FILE"

# Collect CPU usage
echo "=== CPU Usage ===" >> "$LOG_FILE"
top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{usage=100 - $1; print "CPU Usage: " usage "%"}' >> "$LOG_FILE"

echo -e "" >> "$LOG_FILE"

# Collect memory usage
echo "=== Memory Usage ===" >> "$LOG_FILE"
free -h | awk 'NR==2{print "Total: " $2 ", Used: " $3}' >> "$LOG_FILE"

echo -e "" >> "$LOG_FILE"


# Collect disk usage
echo "=== Disk Usage ===" >> "$LOG_FILE"
df -h | awk '$NF=="/"{printf "Total: %s, Used: %s\n", $2, $3}' >> "$LOG_FILE"

echo -e "" >> "$LOG_FILE"


# Collect network interface info
echo "=== Network Interfaces ===" >> "$LOG_FILE"
ip addr show | grep 'state' >> "$LOG_FILE"

echo -e "" >> "$LOG_FILE"


# Collect process information
echo "=== Running Processes ===" >> "$LOG_FILE"
ps aux --sort=-%mem | head -n 10 >> "$LOG_FILE"  # Top 10 memory-consuming processes

echo -e "" >> "$LOG_FILE"


# Collect open files
echo -e "=== Open Files ===" >> "$LOG_FILE"
lsof | wc -l | awk '{print "Open Files Count: " $1}' >> "$LOG_FILE"