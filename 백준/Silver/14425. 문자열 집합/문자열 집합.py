import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = []
s = []

for _ in range(N) : S.append(input().strip())
for _ in range(M) : s.append(input().strip())

cnt = 0
for x in s :
    if x in S : cnt += 1

print(cnt)