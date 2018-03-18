#!/bin/python3

import os
import sys

#
# Complete the aVeryBigSum function below.
#
def aVeryBigSum(n, ar):
    #
    # Write your code here.
    #
    iteration = 0
    bigsum = 0
    while iteration < n:
        bigsum = bigsum + ar[iteration]
        iteration = iteration + 1

    return bigsum

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(n, ar)

    f.write(str(result) + '\n')

    f.close()

