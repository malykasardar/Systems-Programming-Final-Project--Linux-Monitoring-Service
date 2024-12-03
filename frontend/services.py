import subprocess
import re
import os
import time
import requests

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"  # Replace with your Slack Incoming Webhook URL

# Function to call the system resources script and read log output
def call_system_resources():
    # Set the log path directly in the root project directory
    log_path = os.path.join(os.path.dirname(__file__), '..', 'resource_monitoring.log')  # Log file is now in the root directory
    
    # Run the shell script from the correct location
    script_path = os.path.join(os.path.dirname(__file__), '..', 'backend', 'system_resources.sh')  # Correct path to system_resources.sh
    subprocess.run(['bash', script_path])
    time.sleep(0.2)  # Wait for the script to finish and the log file to be updated
    
    # Check if the log file exists, if not, create it (though this shouldn't happen if subprocess is working properly)
    if not os.path.exists(log_path):
        with open(log_path, 'w'):  # Create an empty log file if it doesn't exist
            pass
    
    # Read the log file in the root directory
    with open(log_path, 'r') as log_file:
        return log_file.read()

def track_cpu():
    resources_output = call_system_resources()
    cpu_usage = re.search(r'CPU Usage: ([\d\.]+)%', resources_output)
    return float(cpu_usage.group(1)) if cpu_usage else 0.0

def track_memory():
    resources_output = call_system_resources()
    memory_usage = re.search(r'Total: ([\d\.]+Gi), Used: ([\d\.]+Mi)', resources_output)
    return float(memory_usage.group(2).replace("Mi", "")) / 1024 if memory_usage else 0.0  # Convert Mi to Gi

def track_disk():
    resources_output = call_system_resources()
    disk_usage = re.search(r'Total: (\d+G), Used: ([\d\.]+G)', resources_output)
    return f"Disk Usage: Total: {disk_usage.group(1)}, Used: {disk_usage.group(2)}" if disk_usage else "Disk Usage: Unknown"

def send_slack_notification(message):
    payload = {
        "text": message
    }
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    if response.status_code != 200:
        print(f"Error sending notification to Slack: {response.status_code}, {response.text}")

def track_resources(cpu_threshold, memory_threshold):
    """Monitor system resources and send Slack notifications if thresholds are exceeded."""
    try:
        while True:
            os.system('clear')  # Clear the terminal for a real-time feel
            cpu_usage = track_cpu()
            memory_usage = track_memory()
            disk_usage = track_disk()

            # Print the current usage
            print(f"=== System Resources ===")
            print(f"CPU Usage: {cpu_usage}%")
            print(f"Memory Usage: {memory_usage} Gi")
            print(disk_usage)
            
            # Check if CPU usage exceeds the threshold
            if cpu_usage > cpu_threshold:
                send_slack_notification(f"Warning: CPU usage has exceeded the threshold! Current: {cpu_usage}%")
            
            # Check if memory usage exceeds the threshold
            if memory_usage > memory_threshold:
                send_slack_notification(f"Warning: Memory usage has exceeded the threshold! Current: {memory_usage} Gi")
            
            time.sleep(3.5)  # Refresh every 3.5 seconds
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
