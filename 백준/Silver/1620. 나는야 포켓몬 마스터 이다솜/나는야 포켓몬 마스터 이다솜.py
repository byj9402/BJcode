import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poketmon = {}

for i in range(1, N + 1) :
    name = input().strip()
    poketmon[name] = i

#피카피카피카피
reverse_poketmon = dict(map(reversed, poketmon.items()))

#피카피카피
for _ in range(M) :
    Q = input().strip()
    if Q in poketmon.keys() : print(poketmon[Q])
    else : print(reverse_poketmon[int(Q)])