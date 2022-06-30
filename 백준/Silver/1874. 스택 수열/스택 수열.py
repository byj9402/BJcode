import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
stack = [i + 1 for i in range(N)]
stack = deque(stack)
temp = deque([0])
result = []

sample = []
for _ in range(N) :
    sample.append(int(input()))

i = 0
while (stack) :
    temp.append(stack.popleft())
    result.append('+')
    while (temp[-1] == sample[i]) :
        temp.pop()
        result.append('-')
        i += 1
        if len(temp) == 0 : break
        if i == N : break
    
if result.count('-') != N : print('NO')
else : print('\n'.join(result))