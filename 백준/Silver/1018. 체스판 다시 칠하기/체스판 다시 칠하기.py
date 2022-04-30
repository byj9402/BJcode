import sys
input = sys.stdin.readline

N, M = map(int,input().split())
chess = ['0' * M for _ in range(N)]
for i in range(N) :
    chess[i] = input().rstrip()

paint = []
for i in range(0, N - 7) :
    for j in range(0, M - 7) :
        cnt = 0
        for n in range(i, i + 8) :
            for m in range(j, j + 8) :
                if n % 2 == 0 :
                    if m % 2 == 0 and chess[n][m] != 'B' : cnt += 1
                    if m % 2 != 0 and chess[n][m] == 'B' : cnt += 1
                if n % 2 != 0 :
                    if m % 2 == 0 and chess[n][m] != 'W' : cnt += 1
                    if m % 2 != 0 and chess[n][m] == 'W' : cnt += 1
        paint.append(cnt)

        cnt = 0
        for n in range(i, i + 8) :
            for m in range(j, j + 8) :
                if n % 2 != 0 :
                    if m % 2 == 0 and chess[n][m] != 'B' : cnt += 1
                    if m % 2 != 0 and chess[n][m] == 'B' : cnt += 1
                if n % 2 == 0 :
                    if m % 2 == 0 and chess[n][m] != 'W' : cnt += 1
                    if m % 2 != 0 and chess[n][m] == 'W' : cnt += 1
        paint.append(cnt)

print(min(paint))