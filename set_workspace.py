import os
import platform
import subprocess

# Define the directory where the setup scripts are located
script_directory = "linux_env_setup"

# Define the script names for each OS
macos_script = "macOS_set_linux_env.sh"
windows_script = "windows_set_linux_env.bat"

# Get the OS type
os_type = platform.system()

# Function to run a script
def run_script(script):
    try:
        subprocess.run(script, check=True, shell=True)
        print(f"Successfully ran: {script}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script}: {e}")

# Check the OS and run the corresponding script
if os_type == "Darwin":  # macOS
    script_path = os.path.join(script_directory, macos_script)
    run_script(f"bash {script_path}")  # Run the macOS script using bash

elif os_type == "Windows":  # Windows
    script_path = os.path.join(script_directory, windows_script)
    run_script(f"start cmd /k {script_path}")  # Open a command prompt and run the Windows script

else:
    print(f"Unsupported OS: {os_type}")
