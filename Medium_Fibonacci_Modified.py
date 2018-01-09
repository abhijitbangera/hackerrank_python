'''
Fibonacci Modified
Question: https://www.hackerrank.com/challenges/fibonacci-modified/problem
'''
#!/bin/python3

import sys

def fibonacciModified(t1, t2, n):
    for i in range(n-2):
        f=t1+t2*t2
        t1=t2
        t2=f
    return f
    # Complete this function

if __name__ == "__main__":
    t1, t2, n = input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    result = fibonacciModified(t1, t2, n)
    print(result)
