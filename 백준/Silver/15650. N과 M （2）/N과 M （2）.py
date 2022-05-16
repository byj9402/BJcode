import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = []

def dfs(start) :
    if len(num) == M :
        print(*num)
        return
    
    for i in range(start, N + 1) :
        if i not in num :
            num.append(i)
            dfs(i+1)
            num.pop()

dfs(1)