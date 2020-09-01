#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    dig = last_digit * (-1)
else:
    dig = last_digit
st = "Last digit of "
if dig > 5:
    print(st + "{:d} is {:d} and is greater than 5".format(number, dig))
elif dig == 0:
    print(st + "{:d} is {:d} and is 0".format(number, dig))
elif dig < 6 and dig is not 0:
    print(st + "{:d} is {:d} and is less than 6 and not 0".format(number, dig))
