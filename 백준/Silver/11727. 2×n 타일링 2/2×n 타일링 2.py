import sys
input = sys.stdin.readline

tile = [0, 1, 3]
N = int(input())
if N < 3 : print(tile[N])
else :
    for i in range(3, N + 1) :
        tile.append(tile[i-2] * 2 + tile[i-1])
    print(tile[N] % 10007)