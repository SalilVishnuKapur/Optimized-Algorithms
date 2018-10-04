#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    #print(queries)
    int_dictt = {}
    freq_dictt = {}
    list = []
    for a in queries:
        if a[0] == 1:
            if a[1] in n_dictt:
                n_dictt[a[1]]+=1
                #print(n_dictt)
            else:
                n_dictt[a[1]] = 1
                #print(n_dictt)
        if a[0] == 2:
            if a[1] in n_dictt:
                if n_dictt[a[1]] != 1:
                    n_dictt[a[1]]-=1
                    #print(n_dictt)
                else:
                    del n_dictt[a[1]]
                    #print(n_dictt)
        if a[0] == 3:
            if a[1] in n_dictt.values():
                list.append(1) 
            else:
                list.append(0)
    return list

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