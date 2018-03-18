#!/bin/python3

import sys

def simpleArraySum(n, ar):
    # Complete this function
    total = 0
    for i in ar:
        total = total + i
    return total

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
