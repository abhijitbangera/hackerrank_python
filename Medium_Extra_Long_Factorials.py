'''
Extra Long Factorials
Question: https://www.hackerrank.com/challenges/extra-long-factorials/problem
'''
import sys

def extraLongFactorials(n):
    # Complete this function
    fact=n
    while n!=1:
        fact=fact * (n-1)
        n=n-1
    print (fact)

if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)
