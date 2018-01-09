'''
Question: https://www.hackerrank.com/challenges/write-a-function/problem
'''
def is_leap(year):
    leap = False
    # Write your logic here
    n=year      
    if n%4==0:
        if n%100==0:
            if n%400==0:
                leap=True
            else:
                leap = False
        else:
            leap = True
    
    return leap