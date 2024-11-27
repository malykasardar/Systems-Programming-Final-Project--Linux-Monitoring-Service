#!/bin/bash

# Creating a logs directory if it doesn't exist
mkdir -p monitoring_logs

# Collecting CPU usage
echo "=== CPU Usage ===" > monitoring_logs/cpu_usage.log
# Using top to get CPU usage in a better way
top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{usage=100 - $1; print "CPU Usage: " usage "%"}' >> monitoring_logs/cpu_usage.log

# Collecting memory usage
echo "=== Memory Usage ===" > monitoring_logs/memory_usage.log
# Extracting total and used memory
free -h | awk 'NR==2{print "Total: " $2 ", Used: " $3}' >> monitoring_logs/memory_usage.log

# Collecting disk usage
echo "=== Disk Usage ===" > monitoring_logs/disk_usage.log
# Extracting total and used disk space
df -h | awk '$NF=="/"{printf "Total: %s, Used: %s\n", $2, $3}' >> monitoring_logs/disk_usage.log

# Collecting network interface info
echo "=== Network Interfaces ===" > monitoring_logs/network_interfaces.log
ip addr show | grep 'state' >> monitoring_logs/network_interfaces.log

# Collecting process information
echo "=== Running Processes ===" > monitoring_logs/process_list.log
ps aux --sort=-%mem | head -n 10 >> monitoring_logs/process_list.log  # Top 10 memory-consuming processes

# Collecting open files
echo "=== Open Files ===" > monitoring_logs/open_files.log
lsof | wc -l >> monitoring_logs/open_files.log  # Count of open files

echo "Data collection completed."