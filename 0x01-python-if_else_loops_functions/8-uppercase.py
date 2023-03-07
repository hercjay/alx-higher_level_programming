#!/usr/bin/python3
# Author - Michael Hercjay Anokwulu

def uppercase(s):
    for c in s:
        # Check if character is lowercase
        if ord('a') <= ord(c) <= ord('z'):
            # Convert lowercase character to uppercase using ASCII code
            # and print without new line
            print(chr(ord(c) - ord('a') + ord('A')), end='')
        else:
            # Print character without modification and without new line
            print(c, end='')
    # Print new line using second print function
    print()
