import sys
import os

# Add the 'frontend' directory to sys.path for easier access to frontend/services.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'frontend'))  # For frontend/services.py

# Get the absolute path to the 'utilities' folder in the root directory for importing utility modules
utilities_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utilities'))
sys.path.insert(0, utilities_path)  # For utilities/cpu_stress.py and memory_stress.py

import services  # Import the services from the frontend
import cpu_stress  # Import the CPU stress module from utilities
import memory_stress  # Import the memory stress module from utilities

def display_welcome_message():
    """Display a welcoming message with an overview of available commands."""
    print("""
Welcome to the System Resources Monitoring Tool!
Here are the commands you can use:

- cpu    : Monitor CPU usage.
- memory : Monitor memory usage.
- disk   : Monitor disk usage.
- resources : Monitor overall system resources (CPU, memory, disk, etc.).
- list   : Show all available commands.
- exit   : Exit the tool.

=================================
Type a command to get started!
    """)

def list_commands():
    """Print the list of available commands again."""
    print("""
Here are the available commands:

- cpu    : Monitor CPU usage.
- memory : Monitor memory usage.
- disk   : Monitor disk usage.
- resources : Monitor overall system resources (CPU, memory, disk, etc.).
- list   : Show all available commands.
- exit   : Exit the tool.

=================================
    """)

def get_thresholds():
    """Prompt the user to set thresholds for CPU and memory usage."""
    cpu_threshold = float(input("Enter CPU usage threshold (in %): ").strip())
    memory_threshold = float(input("Enter memory usage threshold (in Gi): ").strip())
    return cpu_threshold, memory_threshold

def monitor_cpu_usage():
    """Monitor and display CPU usage."""
    print("Starting CPU usage monitoring...")
    cpu_usage = services.track_cpu()  # Get current CPU usage
    print(f"Current CPU Usage: {cpu_usage}%")

def monitor_memory_usage():
    """Monitor and display memory usage."""
    print("Starting memory usage monitoring...")
    memory_usage = services.track_memory()  # Get current memory usage
    print(f"Current Memory Usage: {memory_usage} Gi")

def monitor_disk_usage():
    """Monitor and display disk usage."""
    print("Starting disk usage monitoring...")
    disk_usage = services.track_disk()  # Get current disk usage
    print(f"Disk Usage: {disk_usage}")

def monitor_system_resources(cpu_threshold, memory_threshold):
    """Monitor system resources (CPU, memory, disk) with specified thresholds."""
    print(f"Monitoring system resources with the following thresholds (CPU: {cpu_threshold}%, Memory: {memory_threshold} Gi)...")
    
    # Run CPU and memory stress processes in the background
    cpu_stress_process = cpu_stress.run_cpu_stress_in_background()
    memory_stress_process = memory_stress.run_memory_stress_in_background()

    try:
        services.track_resources(cpu_threshold, memory_threshold)  # Begin resource tracking
    except KeyboardInterrupt:
        # Handle user interruption
        print("\nResource monitoring stopped. Type 'list' to see all commands.")
        # Terminate background stress processes
        cpu_stress_process.terminate()
        cpu_stress_process.join()

        memory_stress_process.terminate()
        memory_stress_process.join()

def handle_command(command):
    """Process the user input command and trigger the corresponding function."""
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
        print("Goodbye! Exiting the Monitoring Tool.")
        exit(0)
    else:
        print("Oops! That’s not a valid command. Please try again.")
        list_commands()

def main():
    """Main function to start the tool and continuously process user input."""
    display_welcome_message()
    while True:
        user_input = input("Enter your command: ").strip().lower()  # Prompt user for a command
        handle_command(user_input)  # Execute the appropriate function based on user input

if __name__ == "__main__":
    main()  # Start the tool when the script is run
