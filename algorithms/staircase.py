#!/bin/python3

import sys

def staircase(n):
    # Complete this function
    lines = 1
    while lines < n + 1:
        print((' ' * (n - lines))+('#' * lines))
        lines = lines + 1

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)

