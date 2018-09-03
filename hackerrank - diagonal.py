#!/bin/python3

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    return 'panget'
    #
    # Write your code here.
    #

    if __name__ == '__main__':
        f = open(os.environ['OUTPUT_PATH'], 'w')

        n = int(input())

        a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
