import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
result = [num[0]]

for i in range(len(num) - 1) : result.append(max(result[i] + num[i + 1], num[i + 1]))
print(max(result))