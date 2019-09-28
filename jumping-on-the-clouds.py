#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    #set your counters
    jumps=0
    i=0

    #iterate through the sequence
    while i < len(c)-1:
        # Make sure you don't go out of bounds then check
        # to see if there are any thunderheads
        # I pulled this solution from Nick White on youtube but I couldn't
        # get over the fact that there is a missing test case of the first
        # 2 clouds. But by the rules of the game you can assume either of them
        # are jumpable.
        # My solution was similar except I had if statements of the first two clouds
        # that kept screwing up my counter.
        if i+2 == len(c) or c[i+2] == 1:
            jumps+=1
            i+=1
        else:
            jumps+=1
            i+=2
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
