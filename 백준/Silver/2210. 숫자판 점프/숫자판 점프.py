import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = []
digit = []
for i in range(5) :
    digit.append(list(map(str, input().strip().split())))

def dfs(x, y, temp) :
    if len(temp) == 6 :
        if temp not in result :
            result.append(temp)
        return

    for k in range(4) : 
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5 :
            dfs(nx, ny, temp + digit[nx][ny])

for i in range(5) :
    for j in range(5) :
        dfs(i, j, digit[i][j])

print(len(result))