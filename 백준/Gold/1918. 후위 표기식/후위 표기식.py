import sys
input = sys.stdin.readline

line = list(map(str,(input().strip())))
temp =[]
result = ''

simple = ['+', '-']
unsimple = ['*', '/']

'''
0. 알파벳           -> 순차적으로 result에 삽입
1. 괄호 처리            
2. 특수 취급    (*, /)  -> 괄호와 유사하게 처리
3. 기본 연산자  (+, -)
'''

for a in line:

    if a == '(' :
        temp.append(a)

    elif a in unsimple :
        while temp and temp[-1] in unsimple : result += temp.pop()
        temp.append(a)

    elif a in simple :
        while temp and temp[-1] != '(' : result += temp.pop()
        temp.append(a)

    elif a == ')' :
        while temp and temp[-1] != '(' : result += temp.pop()
        temp.pop()

    else : result += a

while (True) :
    if len(temp) == 0 : break
    result += temp.pop()

print(result)