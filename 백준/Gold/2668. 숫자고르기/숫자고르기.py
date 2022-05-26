import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph, start, i, visited, result) :
    visited[start] = True
    for x in graph[start] :
        if not visited[x] :
            dfs(graph, x, i, visited, result)
        elif visited[x] and x == i :
            result.append(x)

N = int(input())
num = [[] for i in range(N + 1)]
for i in range(N) :
    num[i+1].append(int(input()))

result = []
for i in range(1, N + 1) :
    visited = [False] * (N + 1)
    dfs(num, i, i, visited, result)

print(len(result))
for i in range(len(result)) : print(result[i])