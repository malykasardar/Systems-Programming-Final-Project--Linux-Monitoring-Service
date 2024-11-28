@echo off

:: Change to the parent directory of the script (host machine)
cd /d "%~dp0\.."

:: Set the current directory as the workspace (the parent directory of the script)
set WORKSPACE_DIR=%cd%

:: Ensure Docker is running (this checks if the Docker daemon is up)
docker info >nul 2>&1
if errorlevel 1 (
    echo Docker is not running. Please start Docker.
    exit /b 1
)

:: Run the Docker container, mounting the parent directory as /workspace and start a bash shell in /workspace
docker run --rm -it -v "%WORKSPACE_DIR%:/workspace" ubuntu:latest bash -c "cd /workspace && exec bash"
