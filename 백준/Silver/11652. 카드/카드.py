import sys
input = sys.stdin.readline

num = {}

for _ in range(int(input())) :
    x = int(input())
    if x not in num : num[x] = 1
    else : num[x] = num[x] + 1

num = sorted(num.items(), key = lambda x:(-x[1], x[0]))

print(num[0][0])