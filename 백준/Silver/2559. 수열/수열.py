import sys
input = sys.stdin.readline
N, K = map(int, input().split())
temp = list(map(int, input().split()))
result = []
result.append(sum(temp[0:K]))
for i in range(K, N) :
    num = result[-1] + temp[i] - temp[i - K]
    result.append(num)
print(max(result))