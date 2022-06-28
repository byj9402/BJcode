import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

N = int(input())

## 입력
temp = []
for _ in range(N) :
    temp.append(list(map(str, input().strip())))

## map
field = [['.'] * N for _ in range(N)]

for i in range(N) :
    for j in range(N) :
        if temp[i][j] == '.' :
            sum = 0
            for k in range(8) :
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N :
                    if temp[nx][ny] != '.' :
                        sum += int(temp[nx][ny])
            if sum >= 10 : 
                field[i][j] = 'M'
            else :
                field[i][j] = str(sum)
        else :
            field[i][j] = '*'

for i in range(N) :
    print(''.join(field[i]))