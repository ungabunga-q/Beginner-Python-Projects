def stopwatch():
"""
Stopwatch
-------------------
This program acts as a simple stopwatch using the time module.

Steps for Beginners:
1. Import the time module to work with time-related functions.
2. Wait for the user to press Enter to start the stopwatch.
3. Record the start time using time.time().
4. Wait for the user to press Enter again to stop the stopwatch.
5. Record the end time and calculate the elapsed time.
6. Print the elapsed time.
"""

# 1. Import the time module
import time

# 2. Define the stopwatch function
def stopwatch():
    # 2. Wait for user to start
    input("Press Enter to start the stopwatch...")
    # 3. Record start time
    start = time.time()
    # 4. Wait for user to stop
    input("Press Enter to stop the stopwatch...")
    # 5. Record end time
    end = time.time()
    # 6. Print elapsed time
    print(f"Elapsed time: {end - start:.2f} seconds")

# 3. Main program
if __name__ == "__main__":
    stopwatch()
