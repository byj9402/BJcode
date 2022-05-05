import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = dict()
cnt = 0

for _ in range(N) : dic[input().strip()] = True
for _ in range(M) :
    S = input().strip()
    if S in dic.keys() : cnt += 1

print(cnt)