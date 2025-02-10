import time
import os
import math

# Convert a number into a binary string
# For example: decToBin(25) should return "11001"
# Make sure that decToBin(0) returns "0"
def decToBin(n):
    return "0"

# Useful pieces:
# 
# time.sleep(n)      : Pause the program for n seconds
# time.time()        : Time elapsed (seconds) since midnight on January 1, 1970
# math.floor(n)      : Round a number n down to get an integer
# os.system("clear") : Clear the console

# Loop forever
while True:
    timeStr = "0"
    print("time: ", timeStr.rjust(10)) # Right-justify timeStr to length 10
    time.sleep(0.1) # Pause for 100ms
