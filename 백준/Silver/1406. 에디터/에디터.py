import sys
from collections import deque
input = sys.stdin.readline

lineLeft = deque(input().rstrip())
lineRight = deque()
for i in range(int(input())) :
    command = list(map(str, input().strip().split(' ')))
    if command[0] == 'L' :
        if lineLeft : 
            lineRight.appendleft(lineLeft.pop())
    elif command[0] == 'D' :
        if lineRight : 
            lineLeft.append(lineRight.popleft())
    elif command[0] == 'B' :
        if lineLeft :
            lineLeft.pop()
    elif command[0] == 'P' :
        lineLeft.append(command[1])

lineLeft = list(lineLeft)
lineRight = list(lineRight)

print(''.join(lineLeft), end = '')
print(''.join(lineRight))