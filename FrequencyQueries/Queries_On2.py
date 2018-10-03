#!/bin/python3

import os
import sys


def operation1(dic, word, dic_c):
    if (word in dic) and (dic[word] in dic_c):
        #if dic_c[dic[word]] > 0:
        dic_c[dic[word]] -= 1
    dic[word] = dic.get(word, 0) + 1
    dic_c[dic[word]] = dic_c.get(dic[word], 0) + 1
    return dic, dic_c

def operation2(dic, word, dic_c):
    if word in dic:
        if dic[word] > 0:
            #if dic_c[dic[word]] > 0:
            dic_c[dic[word]] -= 1
            dic[word] -= 1
            dic_c[dic[word]] = dic_c.get(dic[word], 0) + 1
    return dic, dic_c
    
def operation3(arr, freq, dic_c):
    arr.append(dic_c.get(freq, 0) > 0)
    return arr

def freqQuery(queries):
    arr = []
    dic = {}
    dic_c = {}
    for command, word in queries:
        if(command == 1):
            dic, dic_c = operation1(dic, word, dic_c)
        elif(command == 2):
            dic, dic_c = operation2(dic, word, dic_c)
        else:
            arr = operation3(arr, word, dic_c)
    return map(int, arr)
        
    

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
