#!/bin/python3

import os
import sys
from array import array


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
<<<<<<< HEAD:FrequencyQueries/Queries_On2.py
    dic_c = {}
    for command, word in queries:
        if(command == 1):
            dic, dic_c = operation1(dic, word, dic_c)
        elif(command == 2):
            dic, dic_c = operation2(dic, word, dic_c)
        else:
            arr = operation3(arr, word, dic_c)
    return map(int, arr)
        
    
=======
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
>>>>>>> db22959132d53983f9887e2e8aaa1b6087e3d635:FrequencyQueries/Queries_SVK_On2.py

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

