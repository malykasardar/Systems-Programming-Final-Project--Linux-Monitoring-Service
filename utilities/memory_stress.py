import time
import multiprocessing

def memory_stress():
    """Function that continuously consumes memory to stress the system."""
    large_list = []  # Initialize an empty list to hold the large strings
    while True:
        # Allocate a large string (1MB) and add it to the list to use memory
        large_list.append(' ' * 10**6)  # Allocate a 1MB string
        time.sleep(0.1)  # Pause slightly between allocations to avoid crashing immediately

def run_memory_stress_in_background():
    """Launch the memory stress task as a background process."""
    process = multiprocessing.Process(target=memory_stress)  # Create a new process to run the memory stress function
    process.daemon = True  # Ensure that the background process ends when the main program exits
    process.start()  # Start the memory stress process in the background
    return process  # Return the process object in case you need to interact with it later
