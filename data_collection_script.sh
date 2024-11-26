#!/bin/bash

# Create a logs directory if it doesn't exist
mkdir -p monitoring_logs

# Collect CPU usage
echo "=== CPU Usage ===" > monitoring_logs/cpu_usage.log
# Extracting CPU usage percentage (Mac-specific command)
top -l 1 | grep "CPU usage" | awk '{print $3 " " $4 " " $5 " " $6 " " $7 " " $8}' >> monitoring_logs/cpu_usage.log

# Collect memory usage
echo "=== Memory Usage ===" > monitoring_logs/memory_usage.log
# Extracting total and used memory (Mac-specific command)
free -h | awk 'NR==2{print "Total: " $2 ", Used: " $3}' >> monitoring_logs/memory_usage.log

# Collect disk usage
echo "=== Disk Usage ===" > monitoring_logs/disk_usage.log
# Extracting total and used disk space
df -h | awk '$NF=="/"{printf "Total: %s, Used: %s\n", $2, $3}' >> monitoring_logs/disk_usage.log

# Collect network interface info
echo "=== Network Interfaces ===" > monitoring_logs/network_interfaces.log
ip addr show | grep 'state' >> monitoring_logs/network_interfaces.log

# Collect process information
echo "=== Running Processes ===" > monitoring_logs/process_list.log
ps aux --sort=-%mem | head -n 10 >> monitoring_logs/process_list.log  # Top 10 memory-consuming processes

# Collect open files
echo "=== Open Files ===" > monitoring_logs/open_files.log
lsof | wc -l >> monitoring_logs/open_files.log  # Count of open files

echo "Data collection completed."

