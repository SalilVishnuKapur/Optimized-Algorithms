#!/bin/python3

import math
import os
import random
import re
import sys
from array import array

# Complete the freqQuery function below.
def freqQuery(queries):
    '''
    param:
    queries : the different tuple commands
    return : 1 if an element with frequency occurs 0 if not
    '''
    dic = {}
    dic['Chief'] = array('i')
    for item in queries:
        if(item[0] == 1):
            if item[1] not in dic:
                dic[item[1]] = 1
            else:
                dic[item[1]] += 1
        elif(item[0] == 2):
            if item[1] in dic:
                dic[item[1]] -= 1
                if(dic[item[1]] == 0):
                    del dic[item[1]]
        else:
            if(item[1] in set(dic.values())):
                dic['Chief'].append(1)
            else:
                dic['Chief'].append(0)        
    return dic['Chief']

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

