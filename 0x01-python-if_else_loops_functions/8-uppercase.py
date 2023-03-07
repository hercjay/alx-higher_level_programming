#!/usr/bin/python3
# Author - Michael Hercjay Anokwulu

def uppercase(s):
    for i in s:
        c = ord(i)
        if c >= 97 and c <= 122:
            c -= 32
        print("{:c}".format(c), end="")
    print("")
