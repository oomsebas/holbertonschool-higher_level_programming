#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number)%10
if number < 0:
    print_digit = last_digit * (-1)
else:
    print_digit = last_digit
if print_digit > 5 :
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, print_digit))
elif print_digit  == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, print_digit))
elif print_digit < 6 and print_digit is not 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, print_digit))
