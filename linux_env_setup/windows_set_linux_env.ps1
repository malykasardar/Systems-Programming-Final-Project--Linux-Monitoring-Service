# Ensure WSL is installed
if (!(wsl --list)) {
    Write-Output "Installing WSL..."
    wsl --install
    Start-Sleep -Seconds 10 # Allow time for the installation to complete
}

# Check if Ubuntu is installed
if (!(wsl --list | Select-String -Pattern "Ubuntu")) {
    Write-Output "Installing Ubuntu for WSL..."
    wsl --install -d Ubuntu
    Start-Sleep -Seconds 10 # Allow time for Ubuntu installation
}

# Update package lists and install iproute2 and lsof
Write-Output "Updating package lists and installing iproute2 and lsof..."
wsl -d Ubuntu -e sh -c "
    sudo apt update && \
    sudo apt upgrade -y && \
    sudo apt install -y iproute2 lsof
"

# Configure VS Code to use WSL
$settingsPath = "$env:APPDATA\Code\User\settings.json"
if (Test-Path $settingsPath) {
    $settings = Get-Content $settingsPath -Raw | ConvertFrom-Json
    $settings."terminal.integrated.defaultProfile.windows" = "WSL"
    $settings | ConvertTo-Json -Depth 3 | Set-Content $settingsPath
    Write-Output "VS Code terminal is now set to WSL by default."
} else {
    Write-Output "VS Code settings file not found. Please configure manually if needed."
}

Write-Output "Linux environment setup complete!"