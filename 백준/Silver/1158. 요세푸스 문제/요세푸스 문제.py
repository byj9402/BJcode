from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque()
for i in range(1, N+1) : queue.append(i)
cnt = 0

print("<", end = '')
while len(queue) != 1 :
    cnt += 1
    if cnt == K :
        cnt = 0
        print(queue[0], end = ', ')
        queue.popleft()
    else :
        queue.append(queue[0])
        del queue[0]
print(queue[0], end = '')
print('>')