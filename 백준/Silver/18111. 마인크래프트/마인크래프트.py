import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
field = []
result = []

for i in range(N) :
    field += (map(int, input().split()))

for height in range(min(field), max(field) + 1) :
    block = B
    time = 0
    for line in field :
        if (line - height) > 0 :
            block += (line - height)
            time += 2 * (line - height)
        elif (line - height) < 0 :
            block += (line - height)
            time += 1 * (line - height) * (-1)
    if block >= 0 :
        result.append([time, height])

result.sort(key = lambda x:x[1], reverse = True)
result.sort(key = lambda x:x[0])

print(*result[0])