# Monitoring Service

*Systems Programming Final Project - Fall 2024*

## Prerequisites

- **Docker**; Make sure you have docker downloaded for MacOS systems

## MacOS Setup
  **Navigate to linux_environment_setup**
    ```bash
      cd linux_environment_setup
      ```

  **Set linux workspace**
    ```bash
      ./setMacOsWorkspace.sh
      ```

  **Activate Python environment**
    ```bash
    source /workspace/venv/bin/activate
    ```

  **Install requests dependency**
    ```bash
    pip install requests
    ```

## Windows/Ubuntu Setup
  **Setup and activate Python environment in project root**
    ```bash
    apt install -y python3-venv
    python3 -m venv myenv
    source myenv/bin/activate
    ```

  **Install requests dependency**
    ```bash
    pip install requests
    ``` 


## Run the project
  **Run the following command from the root of the project**
    ```bash
    python frontend/main.py
    ```
