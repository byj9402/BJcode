import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
material = list(map(int, input().split()))
material.sort()

cnt = 0

i, j = 0, N - 1
while i < j:
    if material[i] + material[j] == M :
        cnt += 1
        i += 1
        j -= 1
    elif material[i] + material[j] < M : i += 1
    else : j -= 1
    
print(cnt)