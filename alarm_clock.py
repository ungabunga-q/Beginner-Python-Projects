"""
Simple Alarm Clock
Plays a sound after a set time (prints message for simplicity).
"""
import time

def alarm(seconds):
    print(f"Alarm set for {seconds} seconds.")
    time.sleep(seconds)
    print("Time's up! Wake up!")

if __name__ == "__main__":
    secs = int(input("Set alarm for how many seconds? "))
    alarm(secs)
