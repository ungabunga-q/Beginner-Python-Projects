"""
Simple Stopwatch
Counts elapsed time until stopped.
"""
import time

def stopwatch():
    input("Press Enter to start...")
    start = time.time()
    input("Press Enter to stop...")
    end = time.time()
    print(f"Elapsed time: {end - start:.2f} seconds")

if __name__ == "__main__":
    stopwatch()
