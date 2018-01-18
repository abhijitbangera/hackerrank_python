'''
Challenge: Counting Sort 1
URL: https://www.hackerrank.com/challenges/countingsort1/problem
'''

#!/bin/python3

import sys

def countingSort(arr):
    # Complete this function
    d={}
    m=arr
    for i in m:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    x=[]
    for i in range(100):

        if i in d.keys():
            x.append(d[i])
        else:
            x.append(0)
    return x

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))
