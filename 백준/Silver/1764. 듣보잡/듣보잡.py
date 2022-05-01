import sys
input = sys.stdin.readline

N, M = map(int, input().split())
noHeard = [input().strip() for i in range(N)]
noSeen = [input().strip() for i in range(M)]

noHeardSeen = list(set(noHeard) & set(noSeen))
noHeardSeen.sort()

print(len(noHeardSeen))
for i in range(len(noHeardSeen)) : print(noHeardSeen[i])