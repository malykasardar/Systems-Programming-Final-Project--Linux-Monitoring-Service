#!/bin/bash

# Define the log file to store system resource data
LOG_FILE="resource_monitoring.log"

# Clear the log file at the start to ensure it's fresh
> "$LOG_FILE"

# Collect and log CPU usage information
echo "=== CPU Usage ===" >> "$LOG_FILE"
top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{usage=100 - $1; print "CPU Usage: " usage "%"}' >> "$LOG_FILE"

# Add a blank line for better readability
echo -e "" >> "$LOG_FILE"

# Collect and log memory usage
echo "=== Memory Usage ===" >> "$LOG_FILE"
free -h | awk 'NR==2{print "Total: " $2 ", Used: " $3}' >> "$LOG_FILE"

# Add a blank line for better readability
echo -e "" >> "$LOG_FILE"

# Collect and log disk usage
echo "=== Disk Usage ===" >> "$LOG_FILE"
df -h | awk '$NF=="/"{printf "Total: %s, Used: %s\n", $2, $3}' >> "$LOG_FILE"

# Add a blank line for better readability
echo -e "" >> "$LOG_FILE"

# Collect and log network interface information
echo "=== Network Interfaces ===" >> "$LOG_FILE"
ip addr show | grep 'state' >> "$LOG_FILE"

# Add a blank line for better readability
echo -e "" >> "$LOG_FILE"

# Collect and log top 10 memory-consuming processes
echo "=== Running Processes ===" >> "$LOG_FILE"
ps aux --sort=-%mem | head -n 10 >> "$LOG_FILE"  # Display the top 10 processes by memory usage

# Add a blank line for better readability
echo -e "" >> "$LOG_FILE"

# Collect and log the number of open files
echo -e "=== Open Files ===" >> "$LOG_FILE"
lsof | wc -l | awk '{print "Open Files Count: " $1}' >> "$LOG_FILE"
