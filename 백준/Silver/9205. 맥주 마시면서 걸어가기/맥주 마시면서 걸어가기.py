from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def bfs(start, finish) :
    queue = deque()
    queue.append(start)
    while queue :
        x, y = queue.popleft()
        if abs(x - finish[0]) + abs(y - finish[1]) <= 1000 :
            return "happy"
        for i in range(N) :
            if not visited[i] :
                nx, ny = market[i]
                if abs(x - nx) + abs(y - ny) <= 1000 :
                    queue.append((nx, ny))
                    visited[i] = True
    return "sad"

for _ in range(int(input())) :
    N = int(input())
    house = list(map(int, input().split()))
    market = []
    for i in range(N) :
        market.append(list(map(int, input().split())))
    finish = list(map(int, input().split()))
    visited = [False] * (N + 1)
    print(bfs(house, finish))
    