import services
from init_database import init_database
import os
import stat

def display_welcome_message():
    print("""
Welcome to the Monitoring Tool!
=================================
Legend of Commands:
1. apache        - Monitor Apache service.
2. mysql         - Monitor MySQL service.
3. nginx         - Monitor Nginx service.
4. resources     - Monitor system resources (CPU, memory, disk, etc.)
5. sys_utils     - Monitor system utilities.
6. network_sec   - Monitor network and security services.
7. services      - Monitor all registered services.
8. apps          - Monitor running applications.
9. all           - Monitor all available metrics.
10. list         - List all available commands.
11. exit         - Exit the tool.
=================================
Type a command to begin monitoring.
    """)

def list_commands():
    print("""
Available Commands:
1. apache        - Monitor Apache service.
2. mysql         - Monitor MySQL service.
3. nginx         - Monitor Nginx service.
4. resources     - Monitor system resources (CPU, memory, disk, etc.)
5. sys_utils     - Monitor system utilities.
6. network_sec   - Monitor network and security services.
7. services      - Monitor all registered services.
8. apps          - Monitor running applications.
9. all           - Monitor all available metrics.
10. list         - List all available commands.
11. exit         - Exit the tool.
=================================
    """)

def main():
    # Initialize the monitor_logs folder structure before anything else
    init_database()
    print("\n=== Debug: Current Directory Permissions ===")
    for entry in os.listdir():
        if os.path.isdir(entry):  # Check if the entry is a directory
            permissions = os.stat(entry).st_mode
            permission_str = stat.filemode(permissions)
            print(f"Directory: {entry}, Permissions: {permission_str}")

    # Display welcome message and prompt user for commands
    display_welcome_message()
    
    while True:
        user_input = input("Enter a command: ").strip().lower()

        if user_input == "apache":
            print(services.track_apache())  # Print the output to the terminal
        elif user_input == "mysql":
            print(services.track_mysql())
        elif user_input == "nginx":
            print(services.track_nginx())
        elif user_input == "resources":
            try:
                services.track_resources_real_time()  # Calls real-time monitoring
            except KeyboardInterrupt:
                print("\n^C\nReal-time monitoring stopped. Type 'list' to see all available commands.")
                print("Enter a command:", end=" ")
        elif user_input == "sys_utils":
            print(services.track_sys_utils())
        elif user_input == "network_sec":
            try:
                services.track_network_and_security_real_time()  # Calls real-time monitoring
            except KeyboardInterrupt:
                print("\n^C\nReal-time monitoring stopped. Type 'list' to see all available commands.")
                print("Enter a command:", end=" ")
        elif user_input == "services":
            try:
                services.track_services_real_time()  # Calls real-time monitoring
            except KeyboardInterrupt:
                print("\n^C\nReal-time monitoring stopped. Type 'list' to see all available commands.")
                print("Enter a command:", end=" ")
        elif user_input == "apps":
            print(services.track_applications())
        elif user_input == "all":
            try:
                services.track_all_real_time()  # Calls real-time monitoring
            except KeyboardInterrupt:
                print("\n^C\nReal-time monitoring stopped. Type 'list' to see all available commands.")
                print("Enter a command:", end=" ")
        elif user_input == "list":
            list_commands()
        elif user_input == "exit":
            print("Exiting the Monitoring Tool. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
