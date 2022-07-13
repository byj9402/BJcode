import sys
input = sys.stdin.readline

n = int(input())
box = list(map(int, input().split()))
result = [0] * len(box)

for i in range(n) :
    result[i] += 1
    for j in range(i) :
        if box[i] > box[j] :
            result[i] = max(result[i], result[j] + 1)

print(max(result))