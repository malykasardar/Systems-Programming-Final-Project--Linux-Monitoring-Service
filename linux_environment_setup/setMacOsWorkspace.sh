#!/bin/bash

# Define variables
IMAGE_NAME="my_ubuntu_image"
CONTAINER_NAME="my_ubuntu_container"
PARENT_DIR=$(dirname $(pwd)) # Get the parent directory

# Check if Docker is running
is_docker_running() {
    docker info > /dev/null 2>&1
    return $?
}

# Start Docker if it is not running
if ! is_docker_running; then
    echo "Docker is not running. Starting Docker Desktop..."
    open -a Docker
    echo "Waiting for Docker to start..."
    while ! is_docker_running; do
        sleep 1
    done
    echo "Docker is now running."
fi

# Build the Docker image
echo "Building the Docker image: ${IMAGE_NAME}..."
docker build -t ${IMAGE_NAME} .
if [ $? -ne 0 ]; then
    echo "Failed to build the Docker image."
    exit 1
fi
echo "Docker image built successfully."

# Check if a container with the specified name already exists
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo "Container with name ${CONTAINER_NAME} already exists. Removing it..."
    docker rm -f ${CONTAINER_NAME}
fi

# Run the container
echo "Running the Docker container: ${CONTAINER_NAME}..."
docker run --name ${CONTAINER_NAME} -it -v ${PARENT_DIR}:/workspace ${IMAGE_NAME}
if [ $? -ne 0 ]; then
    echo "Failed to start the Docker container."
    exit 1
fi
echo "Docker container is running with parent directory mounted as /workspace."