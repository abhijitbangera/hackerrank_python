'''
Hash Tables: Ransom Note
Question: https://www.hackerrank.com/challenges/ctci-ransom-note/problem
'''
def ransom_note(magazine, ransom):
    for i in magazine:
        if i in ransom:
            ransom.remove(i)
    if not ransom:
        return "Yes"
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    