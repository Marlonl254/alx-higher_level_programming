#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last = number % 10
if last > 5:
    condition = "and is greater than 5"
elif last == 0:
    condition = "and is 0"
else:
    condition = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last} and {condition}")
