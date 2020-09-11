#!/usr/bin/python3
def roman_to_int(roman_string):
    dec = []
    if (roman_string is None or type(roman_string) is not str):
        return 0

    sum = 0
    rom = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    dec = [rom.get(i) for i in roman_string]
    for i, j in zip(dec, dec[1:]):
        if i >= j:
            sum = sum + i
        else:
            sum = sum - i
    sum = sum + dec[-1]
    return sum
