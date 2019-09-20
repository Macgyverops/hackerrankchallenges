#!/bin/python

import math
import os
import random
import re
import sys



# Complete the countingValleys function below.
def countingValleys(n, s):
    #Variables
    #level as in altimeter
    #valleys num of valleys to return, per the exercise it is any descend below sea level (0) and returning to sea level.
    #invalley is a boolean 0=false 1=true to deterime if you are inside a valley
    #vl is an array that pulls the individual string charaters so it can be iterated via a loop.
    #number of steps is ignore as it is not needed for the exercise
    level=0
    valleys=0
    invalley=0
    vl=[char for char in s]

    #iterate through valley list
    for i in vl:
        #first increase or decrease the level based on the step
        if i == 'U':
            level+=1
        elif i == 'D':
             level-=1
        #determine if you've exited a valley
        if level >= 0 and invalley == 1:
                valleys+=1
                invalley=0
        #determine if you are in a valley
        elif level < 0 and invalley == 0:
            invalley=1
    return valleys
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
