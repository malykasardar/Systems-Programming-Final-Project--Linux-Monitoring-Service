#!/bin/bash

# To set up linux, run this command in your vs powershell:
  # .\run_docker.ps1

# Run an Ubuntu Docker container interactively, mount the current directory as /workspace
docker run -it -v ${PWD}:/workspace ubuntu bash -c "
    # Update package lists
    apt-get update && \

    # Install iproute2 and lsof
    apt-get install -y iproute2 lsof && \

    # Change to /workspace directory
    cd /workspace && \

    # Keep the container running interactively
    bash
"