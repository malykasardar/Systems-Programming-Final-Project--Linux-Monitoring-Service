import os
import platform
import subprocess
import time

# Define the directory where the setup scripts are located
script_directory = "linux_env_setup"

# Define the script names for each OS
macos_script = "macOS_set_linux_env.sh"
windows_script = "windows_set_linux_env.bat"

# Get the OS type
os_type = platform.system()

# Function to check if Docker is running
def is_docker_running():
    try:
        # Run a Docker command to check its status
        subprocess.run(["docker", "info"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Function to start Docker
def start_docker():
    try:
        if os_type == "Windows":
            subprocess.run(["start", "docker-desktop"], shell=True, check=True)  # Start Docker Desktop on Windows
        elif os_type == "Darwin":
            subprocess.run(["open", "--background", "/Applications/Docker.app"], check=True)  # Start Docker on macOS
        else:
            subprocess.run(["sudo", "systemctl", "start", "docker"], check=True)  # Start Docker on Linux
        print("Docker start command executed. Waiting for Docker to initialize...")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start Docker: {e}")

# Function to wait until Docker is fully initialized
def wait_for_docker():
    max_retries = 20  # Maximum number of retries (adjustable)
    retry_delay = 5   # Delay in seconds between retries (adjustable)

    for attempt in range(max_retries):
        if is_docker_running():
            print("Docker is now running.")
            return
        print(f"Waiting for Docker to start... (Attempt {attempt + 1}/{max_retries})")
        time.sleep(retry_delay)
    
    # If we exhaust all retries
    print("Docker failed to start after multiple attempts.")
    exit(1)

# Function to run a script
def run_script(script):
    try:
        subprocess.run(script, check=True, shell=True)
        print(f"Successfully ran: {script}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script}: {e}")

# Main logic
if not is_docker_running():
    start_docker()
    wait_for_docker()  # Wait until Docker is fully initialized

# Check the OS and run the corresponding script
if os_type == "Darwin":  # macOS
    script_path = os.path.join(script_directory, macos_script)
    run_script(f"bash {script_path}")  # Run the macOS script using bash

elif os_type == "Windows":  # Windows
    script_path = os.path.join(script_directory, windows_script)
    run_script(f"start cmd /k {script_path}")  # Open a command prompt and run the Windows script

else:
    print(f"Unsupported OS: {os_type}")