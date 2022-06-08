import sys
input = sys.stdin.readline

## 안 되면 15ㄱ
N = int(input())
result = [0, 0, 1]
for i in range(3, N + 1) :
    if i % 2 == 0 : result.append((result[i-1] * 2 + 1) % 1000000007)
    elif i % 2 != 0 : result.append((result[i-1] * 2 - 1) % 1000000007)
print(result[N])