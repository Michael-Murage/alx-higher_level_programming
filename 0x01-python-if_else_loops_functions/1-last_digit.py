#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
y = int(str(number)[-1])


def compare(num):
    x = int(str(num)[-1])
    if (x > 5):
        return "and is greater than 5"
    elif (x == 0):
        return "and is 0"
    elif (x > 0 & x <= 5):
        return "and is less than 6 and not 0"


print(f"Last digit of {number} is {y} {compare(number)}")
