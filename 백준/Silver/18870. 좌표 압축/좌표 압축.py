import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
dic = list(sorted(set(X)))
dic = {dic[i] : i for i in range(len(dic))}

for i in range(N) : X[i] = dic[X[i]]

print(*X)