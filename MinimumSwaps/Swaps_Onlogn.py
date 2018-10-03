#!/bin/python3

import math
import os
import random
import re
import sys

def minimumSwaps(n, arr): 
    '''
    Create a sorted list
    Match case and find odd one out
    Max([unordered digits])
    Min([unordered digits])
    Swap max to the last position
    Swap min to starting position


    2(a).  Match case and find odd one out
    3(a). Max([underdered digits])
    4(a). Min([underdered digits])
    5(a). Swap max to the last position
    6(a). Swap min to starting position

    2(a).  Match case and find odd one out
    3(a). Max([underdered digits])
    4(a). Min([underdered digits])
    5(a). Swap max to the last position
    6(a). Swap min to starting position
    Modified Algo :-
    1. Read the data and create 2 dictionaries
    2. Do min and max and swap and note
    '''
    
    swaps = 0
    dic = {}
    dic_c = {}
    for val, itr in zip(arr, range(n)):
            if itr + 1 != val:
                dic[val] = itr
                dic_c[itr] = val
    
    
    while len(dic) > 1:
        targetVal = min(dic)
        targetIndex = min(dic_c)
        
        if(len(dic) == 2 and dic[targetVal] == targetIndex):
            break
        elif(len(dic) == 2):
            swaps += 1
            break
        
        if(dic[targetVal] != targetIndex):
            tempIndex = dic[targetVal]
            #dic[targetVal] = targetIndex
            dic[dic_c[targetIndex]] = dic[targetVal]

            tempValue = dic_c[targetIndex]
            #dic_c[targetIndex] = targetVal
            dic_c[tempIndex] = dic_c[targetIndex]
            
            if dic[tempValue] == tempIndex + 1:
                del dic[tempValue]
                del dic_c[tempIndex]
            del dic[targetVal]
            del dic_c[targetIndex]
            swaps += 1
        else:
            del dic[targetVal]
            del dic_c[targetIndex]
            
    return swaps  
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    res = minimumSwaps(n, arr)

    fptr.write(str(res) + '\n')

    fptr.close()
