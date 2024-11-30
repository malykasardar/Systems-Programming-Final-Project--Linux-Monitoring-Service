#!/bin/bash

# Define the container name
CONTAINER_NAME="my_ubuntu_container"

# Check if a container with the specified name already exists
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo "Container with name ${CONTAINER_NAME} already exists. Removing it..."
    docker rm -f ${CONTAINER_NAME}
fi

# Run a new Ubuntu Docker container interactively, mount the parent directory as /workspace
echo "Creating a new container named ${CONTAINER_NAME}..."
docker run --name ${CONTAINER_NAME} -it -v $(pwd):/workspace ubuntu bash -c "
    # Update package lists
    apt-get update && \

    # Install iproute2 and lsof
    apt-get install -y iproute2 lsof && \

    # Change to /workspace directory
    cd /workspace && \

    # Keep the container running interactively
    bash
"