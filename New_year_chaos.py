#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q,n):
    # To get to total number of swaps and number of swaps by person we need to reverse all the swaps
    # We start at the beginning of the string and swap characters until they are all in the right order
    # We record the number of swaps as well as how many times each higher digit (per pair) is swaped
    # We will be starting on the first element of the string initially
    i = 0
    swaps = [0]*n
    # print(q)
    # For memory purposes initiate first number of the list that is unsorted. We assume the first element, i.e. 1 (index 0) is not in the right place as we start
    # The nuance here is that i and j might be different e.g. in the list 2,3,1,4 one is not in the right place so, however element 0 (i.e. 2) is in the right place from the point of view of the first iteration (as it is followed by a larger number)
    j = 1
    # While we haven't reached the end of the string
    while i<n-1:
        # If any number is larger it's RHS neighbour
        if q[i] > q[i+1]:
            # Swap the two numbers
            left = q[i+1]
            right = q[i]
            q[i] = left
            q[i+1] = right
            # record a swap was made
            swaps[q[i+1]-1] += 1

            # Avoid reiterating through whole list - start at first element that is not in place
            # Cycle through all list elements starting with the first element that wasn't in the last place in the previous iteration
            for x in range(j-1,len(q)):
                # Once you get to a new element that is not in the right place break the loop
                if q[x] != j:
                    break
                # Otherwise increase the index of the first element that is not in the right place
                j += 1
            # print(j)
            # Next iteration start at the position of the first element that is not in the right place
            i = j-1
        # If the number is smaller than it's RHS neighbout move to the next number
        else:
            i +=1
    # If more than 2 swaps are made for any element return too chaotic
    if max(swaps) > 2:
        print("Too chaotic")
    # Otherwise return sum of swaps for all elements
    else:
        print(sum(swaps))

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q,n)