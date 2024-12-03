import sys
import os
import multiprocessing

# Add the 'frontend' directory and the correct path to 'utilities' to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'frontend'))  # For frontend/services.py

# Use the correct absolute path for 'utilities' directory in the root
utilities_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utilities'))
sys.path.insert(0, utilities_path)  # For utilities/cpu_stress.py and memory_stress.py

# Print sys.path to verify paths are correctly added
print("Current sys.path:", sys.path)

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

def main():
    # Display welcome message and prompt user for commands
    display_welcome_message()
    
    while True:
        user_input = input("Enter a command: ").strip().lower()

        if user_input == "resources":
            # Get thresholds from the user
            cpu_threshold, memory_threshold = get_thresholds()
            
            # Start CPU and Memory stress in the background
            cpu_stress_process = cpu_stress.run_cpu_stress_in_background()
            memory_stress_process = memory_stress.run_memory_stress_in_background()
            
            try:
                services.track_resources(cpu_threshold, memory_threshold)  # Pass thresholds to resource tracking
            except KeyboardInterrupt:
                print("\n^C\nResource monitoring stopped. Type 'list' to see all available commands.")
                print("Enter a command:", end=" ")

                # Stop both CPU and memory stress when user interrupts
                cpu_stress_process.terminate()
                cpu_stress_process.join()

                memory_stress_process.terminate()
                memory_stress_process.join()
                
        elif user_input == "list":
            list_commands()
        elif user_input == "exit":
            print("Exiting the Monitoring Tool. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
