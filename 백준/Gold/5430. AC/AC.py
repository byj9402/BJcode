import sys
from collections import deque
input = sys.stdin.readline

def R(s) : s.reverse()

T = int(input())
for _ in range(T) :
    p = input().strip()
    n = int(input())
    stack = deque(input().strip()[1:-1].split(","))
    
    countR = 0
    countD = 0
    for x in range(len(p)) :
        if p[x] == 'R' : countR += 1
        elif p[x] == 'D' : 
            countD += 1
            if n == 0 or len(stack) == 0 : continue
            elif countR % 2 == 0 : stack.popleft()
            else : stack.pop()
    
    if countR % 2 != 0 : R(stack)
    
    if len(stack) != 0 and n != 0 :
        print('[', end = '')
        for i in range(len(stack) - 1) : print(stack[i], end = ',')
        print(stack[-1], end = '')
        print(']')
    elif n - countD == 0 : print('[]')
    elif n - countD < 0 : print('error')