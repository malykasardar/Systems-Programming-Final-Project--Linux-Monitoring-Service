import time
import multiprocessing

def memory_stress():
    """Function that runs memory-stress indefinitely"""
    large_list = []
    while True:
        # Allocate a large list repeatedly to consume memory
        large_list.append(' ' * 10**6)  # 1MB string allocation
        time.sleep(0.1)  # Slow down the loop slightly to avoid crashing immediately

def run_memory_stress_in_background():
    """Run the memory stress in a background process"""
    process = multiprocessing.Process(target=memory_stress)
    process.daemon = True  # Allow the process to be killed when the main program exits
    process.start()
    return process
