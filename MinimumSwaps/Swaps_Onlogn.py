#!/bin/python3

import math
import os
import random
import re
import sys
    
# Complete the minimumSwaps function below.
def minimumSwaps(arr): 
    '''
    Create a sorted list
    Match case and find odd one out
    Max([underdered digits])
    Min([underdered digits])
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
    '''
    sortedData = sorted(arr)
    flag = True
    swaps = 0
    while flag:
        unMatchDic = {}
        # Match case and find odd one out
        for val, itr in zip(arr, range(len(arr))):
            if(val != sortedData[itr]):
                unMatchDic[val] = itr
                
        if unMatchDic == {}:
            flag = False
            break
        
        if len(unMatchDic) != 2 :
            swaps = swaps++2
        else:
            swaps = swaps++1
        # Max([undordered digits])
        maxVal = max(unMatchDic.keys())

        # Min([undordered digits])
        minVal = min(unMatchDic.keys())

        # Swap max to the last position
        temp = arr[max(unMatchDic.values())]
        arr[max(unMatchDic.values())] = maxVal
        arr[unMatchDic[maxVal]] = temp
        miniTemp = unMatchDic[maxVal]
        unMatchDic[maxVal] = unMatchDic[temp]
        unMatchDic[temp] = miniTemp
        
        if(len(unMatchDic) != 2 ):
            # Swap min to starting position
            temp = arr[min(unMatchDic.values())]
            arr[min(unMatchDic.values())] = minVal
            arr[unMatchDic[minVal]] = temp

    return swaps
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()


