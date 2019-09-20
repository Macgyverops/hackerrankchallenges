#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #sort the array
    ar.sort()
    #set the last sock register to 0 as it is invalid
    lastsock=0
    #initiate the numpairs variable
    numpairs=0
    #iterate through the sock pairs array add them if they match and set the register for last sock to an invalid sock color to prevent a new pair from matching.
    for i in ar:
        if lastsock >= 1 and lastsock <= 100:
            if lastsock == i:
                numpairs=numpairs+1
                i=0
        lastsock=i
    return numpairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

