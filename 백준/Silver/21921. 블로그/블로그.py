import sys
input = sys.stdin.readline

dp = []

N, X = map(int, input().split())
visiter = list(map(int, input().split()))

temp = sum(visiter[0:X])
dp.append(temp)

for i in range(X, N) :
    temp += visiter[i]
    temp -= visiter[i-X]
    dp.append(temp)

result = max(dp)

if result == 0 : print("SAD")
else :
    print(result)
    print(dp.count(result))