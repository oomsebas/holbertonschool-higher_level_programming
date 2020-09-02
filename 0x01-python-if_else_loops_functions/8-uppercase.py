#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        let = ord(letter)
        if ord(letter) >= 97 and ord(letter) <= 122:
            let = let - 32
        print("{}".format(chr(let)), end="")
    print("")
