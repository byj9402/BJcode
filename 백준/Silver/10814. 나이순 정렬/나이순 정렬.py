import sys
input = sys.stdin.readline

N = int(input())
member = [['0', '0'] for i in range(N)]
for i in range(0, N) :
    member[i] = list(map(str, input().split()))

member.sort(key = lambda x : int(x[0]))

for i in range(0, N) : print(*member[i])