import subprocess
import re
import os
import time
import requests

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"  # Replace with your Slack Incoming Webhook URL

def call_system_resources():
    """Run the system resources script and return the contents of the log file."""
    # Define the path for the log file, located in the root project directory
    log_path = os.path.join(os.path.dirname(__file__), '..', 'resource_monitoring.log')
    
    # Set the path to the system resources script in the 'backend' directory
    script_path = os.path.join(os.path.dirname(__file__), '..', 'backend', 'system_resources.sh')
    
    # Run the script
    subprocess.run(['bash', script_path])
    time.sleep(0.5)  # Give it a moment to update the log file
    
    # Check if the log file exists. If not, create an empty one (though this shouldn't happen)
    if not os.path.exists(log_path):
        with open(log_path, 'w'):  # Create the log file if it doesn't exist
            pass
    
    # Read the log file and return its contents
    with open(log_path, 'r') as log_file:
        return log_file.read()

def track_cpu():
    """Retrieve and return the current CPU usage from the system log."""
    resources_output = call_system_resources()
    cpu_usage = re.search(r'CPU Usage: ([\d\.]+)%', resources_output)
    
    return float(cpu_usage.group(1)) if cpu_usage else 0.0

def track_memory():
    """Retrieve and return the current memory usage from the system log."""
    resources_output = call_system_resources()
    memory_usage = re.search(r'Total: ([\d\.]+Gi), Used: ([\d\.]+Mi)', resources_output)
    # Convert memory from Mi to Gi
    return float(memory_usage.group(2).replace("Mi", "")) / 1024 if memory_usage else 0.0

def track_disk():
    """Retrieve and return the current disk usage from the system log."""
    resources_output = call_system_resources()
    disk_usage = re.search(r'Total: (\d+G), Used: ([\d\.]+G)', resources_output)
    # Return disk usage info or a default message if the info is not found
    return f"Total: {disk_usage.group(1)}, Used: {disk_usage.group(2)}" if disk_usage else "Disk Usage: Unknown"

def send_slack_notification(message):
    """Send a Slack notification with the provided message."""
    payload = {
        "text": message  # Format the message for Slack
    }
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)  # Send the message
    if response.status_code != 200:
        print(f"Error sending notification to Slack: {response.status_code}, {response.text}")

def track_resources(cpu_threshold, memory_threshold):
    """Monitor system resources and send Slack notifications if thresholds are exceeded."""
    try:
        while True:
            os.system('clear')  # Clear the terminal screen for a real-time feel
            cpu_usage = track_cpu()  # Track CPU usage
            memory_usage = track_memory()  # Track memory usage
            disk_usage = track_disk()  # Track disk usage

            # Print the current system resource usage
            print(f"=== System Resources ===")
            print(f"CPU Usage: {cpu_usage}%")
            print(f"Memory Usage: {memory_usage} Gi")
            print(disk_usage)

            # Send a Slack notification if the CPU usage exceeds the threshold
            if cpu_usage > cpu_threshold:
                send_slack_notification(f"Warning: CPU usage has exceeded the threshold! Current: {cpu_usage}%")
            
            # Send a Slack notification if the memory usage exceeds the threshold
            if memory_usage > memory_threshold:
                send_slack_notification(f"Warning: Memory usage has exceeded the threshold! Current: {memory_usage} Gi")
            
            time.sleep(3.5)  # Wait for 3.5 seconds before refreshing the data
    except KeyboardInterrupt:
        print("\nSystem monitoring stopped.")