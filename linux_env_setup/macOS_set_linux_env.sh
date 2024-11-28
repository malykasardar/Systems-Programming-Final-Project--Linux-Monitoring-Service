#!/bin/bash

# Run an Ubuntu Docker container interactively, mount the parent directory as /workspace
docker run -it -v $(pwd)/..:/workspace ubuntu bash -c "
    # Update package lists
    apt-get update && \

    # Install iproute2 and lsof
    apt-get install -y iproute2 lsof && \

    # Change to /workspace directory
    cd /workspace && \

    # Keep the container running interactively
    bash
"
