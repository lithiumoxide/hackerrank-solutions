#!/bin/python3

import sys

def extraLongFactorials(n):
    # Complete this function
    i = n
    factorial = 1
    while i > 0:
        factorial = factorial * i
        i = i - 1
    print(factorial)

if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)

