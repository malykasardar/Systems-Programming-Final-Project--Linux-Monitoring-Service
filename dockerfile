# Use the latest Ubuntu image as the base
FROM ubuntu:latest

# Update package lists and install required tools
RUN apt-get update && apt-get install -y \
    iproute2 \
    lsof \
    python3 \
    python3-pip && \
    # Set python3 as the default python
    update-alternatives --install /usr/bin/python python /usr/bin/python3 1 && \
    # Clean up unnecessary files
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /workspace

# Copy the contents of the current directory into the container
COPY . .

# Set the default command
CMD ["bash"]