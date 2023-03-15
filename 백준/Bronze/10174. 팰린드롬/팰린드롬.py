import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for _ in range(T) : 
    pelin = True

    s = input().rstrip()
    s = s.upper()
    s = list(s)
    queue = deque(s)

    for i in range(len(s)-2) :
        a = queue.pop()
        b = queue.popleft()
        if a != b :
            pelin = False
            break
        if len(queue) <= 1 : break

    if pelin : print('Yes')
    else : print("No")