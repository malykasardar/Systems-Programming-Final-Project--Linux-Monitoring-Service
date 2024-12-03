import sys
import os
import multiprocessing
import time

# Add the 'frontend' directory and the correct path to 'utilities' to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'frontend'))  # For frontend/services.py

# Use the correct absolute path for 'utilities' directory in the root
utilities_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utilities'))
sys.path.insert(0, utilities_path)  # For utilities/cpu_stress.py and memory_stress.py

import services  # This will now import from frontend/services.py
import cpu_stress  # Import the CPU stress module from utilities
import memory_stress  # Import the Memory stress module from utilities

def display_welcome_message():
    print("""
Welcome to the System Resources Monitoring Tool!
Legend of Commands:

cpu - Monitor CPU usage.
memory - Monitor memory usage.
disk - Monitor disk usage.
resources - Monitor overall system resources (CPU, memory, disk, etc.).
list - List all available commands.
exit - Exit the tool.
=================================
Type a command to begin monitoring.
    """)

def list_commands():
    print("""
Available Commands:
cpu - Monitor CPU usage.
memory - Monitor memory usage.
disk - Monitor disk usage.
resources - Monitor overall system resources (CPU, memory, disk, etc.).
list - List all available commands.
exit - Exit the tool.
=================================
    """)

def get_thresholds():
    cpu_threshold = float(input("Set CPU usage threshold (in %): ").strip())
    memory_threshold = float(input("Set memory usage threshold (in Gi): ").strip())
    return cpu_threshold, memory_threshold

def monitor_cpu_usage():
    print("Monitoring CPU usage...")
    cpu_usage = services.track_cpu()  # Fetch CPU usage once
    print(f"CPU Usage: {cpu_usage}%")

def monitor_memory_usage():
    print("Monitoring memory usage...")
    memory_usage = services.track_memory()  # Fetch memory usage once
    print(f"Memory Usage: {memory_usage} Gi")

def monitor_disk_usage():
    print("Monitoring disk usage...")
    disk_usage = services.track_disk()  # Fetch disk usage once
    print(disk_usage)

def monitor_system_resources(cpu_threshold, memory_threshold):
    print(f"Monitoring system resources with thresholds (CPU: {cpu_threshold}%, Memory: {memory_threshold} Gi)...")
    # Start CPU and Memory stress in the background
    cpu_stress_process = cpu_stress.run_cpu_stress_in_background()
    memory_stress_process = memory_stress.run_memory_stress_in_background()

    try:
        services.track_resources(cpu_threshold, memory_threshold)
    except KeyboardInterrupt:
        print("\n^C\nResource monitoring stopped. Type 'list' to see all available commands.")
        # Stop both CPU and memory stress when user interrupts
        cpu_stress_process.terminate()
        cpu_stress_process.join()

        memory_stress_process.terminate()
        memory_stress_process.join()

def handle_command(command):
    """Handle user input commands and execute corresponding functions."""
    if command == "cpu":
        monitor_cpu_usage()
    elif command == "memory":
        monitor_memory_usage()
    elif command == "disk":
        monitor_disk_usage()
    elif command == "resources":
        cpu_threshold, memory_threshold = get_thresholds()
        monitor_system_resources(cpu_threshold, memory_threshold)
    elif command == "list":
        list_commands()
    elif command == "exit":
        print("Exiting the Monitoring Tool. Goodbye!")
        exit(0)
    else:
        print("Invalid command. Please try again.")
        list_commands()

def main():
    display_welcome_message()
    while True:
        user_input = input("Enter a command: ").strip().lower()
        handle_command(user_input)

if __name__ == "__main__":
    main()
