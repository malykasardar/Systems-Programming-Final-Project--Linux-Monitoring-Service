import os
import shutil
import stat

def init_database():
    # Define the root folder and its subdirectories/files
    root_folder = 'monitor_logs'
    subdirectories = {
        'application_logs': ['sys_utils.log', 'network_and_security.log'],
        'service_logs': ['mysql_service.log', 'apache_service.log', 'nginx_service.log'],
    }
    log_file = 'resource_monitoring.log'

    # Delete the root folder if it already exists
    if os.path.exists(root_folder):
        shutil.rmtree(root_folder)
        print(f"Deleted existing directory: {root_folder}")

    # Create the root folder with write permissions for all users
    os.makedirs(root_folder)
    os.chmod(root_folder, 0o777)  # Set permissions to allow read/write/execute for everyone
    print(f"Created directory: {root_folder} with permissions 777")
    
    # Create subdirectories and their respective log files
    for subdir, files in subdirectories.items():
        subdir_path = os.path.join(root_folder, subdir)
        os.makedirs(subdir_path)
        os.chmod(subdir_path, 0o777)  # Set permissions to allow read/write/execute for everyone
        print(f"Created directory: {subdir_path} with permissions 777")
        
        # Create the log files within each subdirectory
        for file_name in files:
            file_path = os.path.join(subdir_path, file_name)
            with open(file_path, 'w') as file:
                file.write('')  # Create an empty file
            os.chmod(file_path, 0o666)  # Set permissions to allow read/write for everyone
            print(f"Created file: {file_path} with permissions 666")

    # Create the resource monitoring log file in the root directory
    log_file_path = os.path.join(root_folder, log_file)
    with open(log_file_path, 'w') as file:
        file.write('')  # Create an empty file
    os.chmod(log_file_path, 0o666)  # Set permissions to allow read/write for everyone
    print(f"Created file: {log_file_path} with permissions 666")

if __name__ == "__main__":
    init_database()
