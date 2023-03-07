#!/usr/bin/python3
# Author - Michael Hercjay Anokwulu

def uppercase(s):
    for c in s:
        print(chr(ord(c) - 32), end="")
    print()
