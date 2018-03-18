#!/bin/python3

import sys

def breakingRecords(score):
    # Complete this function
    high = 0
    low = 0
    num_highs = 0
    num_lows = 0
    i = 0
    while i < len(score):
        if score[i] > high:
            num_highs = num_highs + 1
            high = score[i]
        elif score[i] < low:
            num_lows = num_lows + 1
            low = score[i]
        i = i + 1
    print(str(num_highs) + ' ' + str(num_lows))

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))



