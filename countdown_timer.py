def countdown(seconds):
"""
Countdown Timer
-------------------
This program counts down from a given number of seconds.

Steps for Beginners:
1. Import the time module to use sleep for delays.
2. Define a countdown function that takes seconds as input.
3. Use a while loop to update and display the timer every second.
4. Use divmod to get minutes and seconds.
5. Print the timer in mm:ss format and update each second.
6. Print a message when the countdown is finished.
"""

# 1. Import the time module
import time

# 2. Define the countdown function
def countdown(seconds):
    # 3. Loop until seconds reach 0
    while seconds:
        # 4. Get minutes and seconds
        mins, secs = divmod(seconds, 60)
        # 5. Print timer
        print(f"{mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        seconds -= 1
    # 6. Print when done
    print("Time's up!")

# 3. Main program
if __name__ == "__main__":
    secs = int(input("Enter seconds to countdown: "))
    countdown(secs)
