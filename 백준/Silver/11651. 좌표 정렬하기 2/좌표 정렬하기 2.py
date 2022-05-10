import sys
input = sys.stdin.readline

num = []

for _ in range(int(input())) :
    x, y = map(int, input().split())
    num.append((x, y))

num.sort(key = lambda x : (x[1], x[0]))
for i in range(len(num)) : print(num[i][0], num[i][1])