import time
import multiprocessing

def cpu_stress():
    """Keep the CPU busy by performing an infinite computational task."""
    while True:
        _ = 12345 ** 0.5  # A simple computation to continuously stress the CPU

def run_cpu_stress_in_background():
    """Start a background process that runs the CPU stress task."""
    process = multiprocessing.Process(target=cpu_stress)  # Create a new process to run the CPU stress function
    process.daemon = True  # Ensure the process will be terminated when the main program exits
    process.start()  # Start the background process
    return process  # Return the process object in case we need to interact with it later
