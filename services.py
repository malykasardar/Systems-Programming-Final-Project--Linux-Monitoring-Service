import subprocess
import re
import os
import time

# Function to call the MySQL script and read log output
def call_mysql():
    # Store the original working directory
    original_cwd = os.getcwd()

    # Use Popen to execute the script in an isolated manner
    process = subprocess.Popen(['bash', 'mysql.sh'], cwd='monitoring_services/service_monitoring', shell=False)
    process.communicate()  # Wait for the process to complete
    
    # Restore the original working directory to ensure consistency
    os.chdir(original_cwd)

    time.sleep(1)  # Give time for the log to be written

    # Read and return log content
    with open('monitor_logs/service_logs/mysql_service.log', 'r') as log_file:
        return log_file.read()

# Function to call the Apache script and read log output
def call_apache():
    # Store the original working directory
    original_cwd = os.getcwd()

    # Use Popen to execute the script in an isolated manner
    process = subprocess.Popen(['bash', 'apache.sh'], cwd='monitoring_services/service_monitoring', shell=False)
    process.communicate()  # Wait for the process to complete
    
    # Restore the original working directory to ensure consistency
    os.chdir(original_cwd)

    time.sleep(1)  # Give time for the log to be written

    # Read and return log content
    with open('monitor_logs/service_logs/apache_service.log', 'r') as log_file:
        return log_file.read()

# Function to call the Nginx script and read log output
def call_nginx():
    # Store the original working directory
    original_cwd = os.getcwd()

    # Use Popen to execute the script in an isolated manner
    process = subprocess.Popen(['bash', 'nginx.sh'], cwd='monitoring_services/service_monitoring', shell=False)
    process.communicate()  # Wait for the process to complete
    
    # Restore the original working directory to ensure consistency
    os.chdir(original_cwd)

    time.sleep(1)  # Give time for the log to be written

    # Read and return log content
    with open('monitor_logs/service_logs/nginx_service.log', 'r') as log_file:
        return log_file.read()

# Function to call the system resources script and read log output
def call_system_resources():
    subprocess.run(['bash', 'monitoring_services/system_resources.sh'])
    time.sleep(0.2)  # Wait for the script to finish and the log file to be updated
    with open('monitor_logs/resource_monitoring.log', 'r') as log_file:
        return log_file.read()

# Function to call the sys_utils script and read log output
def call_sys_utils():
    subprocess.run(['bash', 'monitoring_services/application_monitoring/sys_utils.sh'])
    time.sleep(0.2)  # Wait for the script to finish and the log file to be updated
    with open('monitor_logs/application_logs/sys_utils.log', 'r') as log_file:
        return log_file.read()

# Function to call the network_and_security script and read log output
def call_network_and_security():
    subprocess.run(['bash', 'monitoring_services/application_monitoring/network_and_security.sh'])
    time.sleep(0.2)  # Wait for the script to finish and the log file to be updated
    with open('monitor_logs/application_logs/network_and_security.log', 'r') as log_file:
        return log_file.read()

# Function to call MySQL, Apache, and Nginx scripts and read log output
def call_services():
    mysql_output = call_mysql()
    apache_output = call_apache()
    nginx_output = call_nginx()
    return mysql_output, apache_output, nginx_output

# Function to call sys_utils and network_and_security scripts and read log output
def call_applications():
    sys_utils_output = call_sys_utils()
    network_security_output = call_network_and_security()
    return sys_utils_output, network_security_output

# Function to call all scripts and read log output
def call_all():
    mysql_output = call_mysql()
    apache_output = call_apache()
    nginx_output = call_nginx()
    system_resources_output = call_system_resources()
    sys_utils_output = call_sys_utils()
    network_security_output = call_network_and_security()
    return mysql_output, apache_output, nginx_output, system_resources_output, sys_utils_output, network_security_output














# Parsing functions for terminal output

def track_apache():
    apache_output = call_apache()
    status = re.search(r'Apache is (\w+)', apache_output)
    if status:
        status = status.group(1)
    else:
        status = "Unknown"

    return f"Apache Service Status: {status}"

def track_mysql():
    mysql_output = call_mysql()
    status = re.search(r'MySQL is (\w+)', mysql_output)
    if status:
        status = status.group(1)
    else:
        status = "Unknown"

    return f"MySQL Service Status: {status}"

def track_nginx():
    nginx_output = call_nginx()
    status = re.search(r'Nginx is (\w+)', nginx_output)
    if status:
        status = status.group(1)
    else:
        status = "Unknown"

    return f"Nginx Service Status: {status}"

def track_resources():
    resources_output = call_system_resources()

    # Parsing the output based on the actual format in resource_monitoring.log
    cpu_usage = re.search(r'CPU Usage: ([\d\.]+)%', resources_output)
    memory_usage = re.search(r'Total: ([\d\.]+Gi), Used: ([\d\.]+Mi)', resources_output)
    disk_usage = re.search(r'Total: (\d+G), Used: ([\d\.]+G)', resources_output)

    # Extract the groups if the pattern matches, otherwise set to "Unknown"
    cpu_usage = cpu_usage.group(1) if cpu_usage else "Unknown"
    memory_usage = f"Total: {memory_usage.group(1)}, Used: {memory_usage.group(2)}" if memory_usage else "Unknown"
    disk_usage = f"Total: {disk_usage.group(1)}, Used: {disk_usage.group(2)}" if disk_usage else "Unknown"

    # Return formatted output
    return f"CPU Usage: {cpu_usage}%\nMemory Usage: {memory_usage}\nDisk Usage: {disk_usage}"


def track_services():
    mysql_status = track_mysql()
    apache_status = track_apache()
    nginx_status = track_nginx()

    return f"{mysql_status}\n{apache_status}\n{nginx_status}"

def track_applications():
    sys_utils_output = call_sys_utils()
    network_security_output = call_network_and_security()

    sys_utils_status = re.search(r'Sys Utils: (.+)', sys_utils_output)
    network_status = re.search(r'Network: (.+)', network_security_output)

    sys_utils_status = sys_utils_status.group(1) if sys_utils_status else "Unknown"
    network_status = network_status.group(1) if network_status else "Unknown"

    return f"System Utilities Status: {sys_utils_status}\nNetwork and Security Status: {network_status}"

def track_all():
    services_status = track_services()
    resources_status = track_resources()
    applications_status = track_applications()

    return f"{services_status}\n{resources_status}\n{applications_status}"













# Real-time monitoring functions
def track_resources_real_time():
    """Monitor system resources in real-time."""
    try:
        while True:
            os.system('clear')  # Clear the terminal for a real-time feel
            resources_data = track_resources()  # Call the static function
            print("=== System Resources ===")
            print(resources_data)
            time.sleep(3.5)  # Refresh every second
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

def track_network_and_security_real_time():
    """Monitor network and security services in real-time."""
    try:
        while True:
            os.system('clear')
            network_data = track_network_and_security()  # Call the static function
            print("=== Real-Time Network and Security Monitoring ===")
            print(network_data)
            time.sleep(3.5)
    except KeyboardInterrupt:
        print("\nReal-time monitoring stopped.")

def track_services_real_time():
    """Monitor all registered services in real-time."""
    try:
        while True:
            os.system('clear')
            services_data = track_services()  # Call the static function
            print("=== Real-Time Services Monitoring ===")
            print(services_data)
            time.sleep(3.5)
    except KeyboardInterrupt:
        print("\nReal-time monitoring stopped.")

def track_all_real_time():
    """Monitor all metrics in real-time."""
    try:
        while True:
            os.system('clear')
            all_data = track_all()  # Call the static function
            print("=== Real-Time Full Monitoring ===")
            print(all_data)
            time.sleep(3.5)
    except KeyboardInterrupt:
        print("\nReal-time monitoring stopped.")
