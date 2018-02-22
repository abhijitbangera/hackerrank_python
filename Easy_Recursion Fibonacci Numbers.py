'''
Recursion: Fibonacci Numbers
Question: https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem
'''
def fibonacci(n):
    a, b = 0, 1
    i = 0
    while i != n:
        a, b = b, a+b
        i = i+1
    return a
n = int(input())
print(fibonacci(n))