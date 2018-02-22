'''
Time Complexity: Primality
Question: https://www.hackerrank.com/challenges/ctci-big-o/problem
'''
p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    if n>1:
        for i in range(2, n//2+1):
            if n%i==0:
                print ("Not prime")
                break
        else:
            print ("Prime")
    else:
        print ("Not prime")