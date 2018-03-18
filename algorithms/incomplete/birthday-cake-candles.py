#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    candles = 0
    i = 0
    while i < n:
        if ar[i] == max(ar):
            candles = candles + 1
        i = i + 1
    return candles

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
