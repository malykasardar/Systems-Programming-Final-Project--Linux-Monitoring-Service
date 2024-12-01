import subprocess
import re

# Function to call the MySQL script and capture output
def call_mysql():
    result = subprocess.run(['bash', 'monitoring_services/service_monitoring/mysql.sh'], capture_output=True, text=True)
    return result.stdout

# Function to call the Apache script and capture output
def call_apache():
    result = subprocess.run(['bash', 'monitoring_services/service_monitoring/apache.sh'], capture_output=True, text=True)
    return result.stdout

# Function to call the Nginx script and capture output
def call_nginx():
    result = subprocess.run(['bash', 'monitoring_services/service_monitoring/nginx.sh'], capture_output=True, text=True)
    return result.stdout

# Function to call the system resources script and capture output
def call_system_resources():
    result = subprocess.run(['bash', 'monitoring_services/system_resources.sh'], capture_output=True, text=True)
    return result.stdout

# Function to call the sys_utils script and capture output
def call_sys_utils():
    result = subprocess.run(['bash', 'monitoring_services/application_monitoring/sys_utils.sh'], capture_output=True, text=True)
    return result.stdout

# Function to call the network_and_security script and capture output
def call_network_and_security():
    result = subprocess.run(['bash', 'monitoring_services/application_monitoring/network_and_security.sh'], capture_output=True, text=True)
    return result.stdout

# Function to call MySQL, Apache, and Nginx scripts and capture output
def call_services():
    mysql_output = call_mysql()
    apache_output = call_apache()
    nginx_output = call_nginx()
    return mysql_output, apache_output, nginx_output

# Function to call sys_utils and network_and_security scripts and capture output
def call_applications():
    sys_utils_output = call_sys_utils()
    network_security_output = call_network_and_security()
    return sys_utils_output, network_security_output

# Function to call all scripts and capture output
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

    cpu_usage = re.search(r'CPU Usage: (\d+)%', resources_output)
    memory_usage = re.search(r'Total: (\d+\.\d+)Gi, Used: (\d+\.\d+)Mi', resources_output)
    disk_usage = re.search(r'Total: (\d+)G, Used: (\d+\.\d+)G', resources_output)

    cpu_usage = cpu_usage.group(1) if cpu_usage else "Unknown"
    memory_usage = f"Total: {memory_usage.group(1)} Gi, Used: {memory_usage.group(2)} Mi" if memory_usage else "Unknown"
    disk_usage = f"Total: {disk_usage.group(1)} G, Used: {disk_usage.group(2)} G" if disk_usage else "Unknown"

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

call_mysql()