import sys
sys.setrecursionlimit(10**6)

N = int(input())
computer = [[] for _ in range(N+1)]
visited = [False] * (N+1)
num = []

def dfs(graph, start, visited, num) :
    visited[start] = True
    for i in graph[start] :
        if not visited[i] :
            num.append(i)
            dfs(graph, i, visited, num)
    return len(num)

for _ in range(int(input())) :
    x, y = map(int, input().split())
    computer[x].append(y)
    computer[y].append(x)

print(dfs(computer, 1, visited, num))