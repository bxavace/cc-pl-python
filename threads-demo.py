""" Python program to demonstrate multiple threads (waste) """
# DON'T RUN THIS PROGRAM! NEED daemon=True and other fix to be able to exit on KeyboardInterrupt.
import os
import threading

def cpu_waster():
    while True:
        pass

print(f"\n\tProcess ID: {os.getpid()}")
print(f"Thread count: {threading.active_count()}")
for thread in threading.enumerate():
    print(thread)

print("\nStarting 10 CPU wasters")
for i in range(10):
    threading.Thread(target=cpu_waster).start()

print(f"\n\tProcess ID: {os.getpid()}")
print(f"Thread count: {threading.active_count()}")
for thread in threading.enumerate():
    print(thread)
