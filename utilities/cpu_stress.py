import time
import multiprocessing

def cpu_stress():
    """Function that runs an infinite CPU-heavy task"""
    while True:
        _ = 12345 ** 0.5  # Perform a computation to keep the CPU busy

def run_cpu_stress_in_background():
    """Run the CPU stress in a background process"""
    process = multiprocessing.Process(target=cpu_stress)
    process.daemon = True  # Allow the process to be killed when the main program exits
    process.start()
    return process
