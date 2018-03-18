#!/bin/python3

import sys

def miniMaxSum(arr):
    # Complete this function
    iterations = len(arr)
    i = 0
    final_list = []
    while i < iterations:
        final_list.append(sum(arr) - arr[i])
        i = i + 1
    print(str(min(final_list)) + ' ' + str(max(final_list)))

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)

