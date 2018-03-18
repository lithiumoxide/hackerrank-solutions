#!/bin/python3

import sys

def diagonalDifference(a):
    # Complete this function
    i = 0
    j = 0
    m = n - 1
    pri_diag_sum = 0
    sec_diag_sum = 0
    
    while i < n:
        pri_diag_sum = pri_diag_sum + a[i][i]
        i += 1
    
    while j < n:
        sec_diag_sum = sec_diag_sum + a[j][m-j]
        j += 1
    
    return abs(pri_diag_sum - sec_diag_sum)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)

