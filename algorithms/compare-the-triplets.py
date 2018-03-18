#!/bin/python3

import os
import sys

#
# Complete the solve function below.
#
def solve(a0, a1, a2, b0, b1, b2):
    #
    # Write your code here.
    #
    alice = [a0, a1, a2]
    bob = [b0, b1, b2]
    alice_score = 0
    bob_score = 0
    i = 0
    
    while i < 3:
        if alice[i] > bob[i]:
            alice_score += 1
        elif alice[i] < bob[i]:
            bob_score += 1
        i += 1
    
    return str(alice_score) + str(bob_score)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a0A1A2 = input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()

