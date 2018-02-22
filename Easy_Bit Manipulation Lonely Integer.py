'''
Bit Manipulation: Lonely Integer
Question: https://www.hackerrank.com/challenges/ctci-lonely-integer/problem
'''
import sys

def lonely_integer(a):
    dict = {}
    for i in a:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    for k,v in dict.items():
        if v == 1:
            return k

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))