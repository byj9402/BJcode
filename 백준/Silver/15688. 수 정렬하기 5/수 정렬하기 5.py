import sys
input = sys.stdin.readline

num = []

for _ in range(int(input())) :
    num.append(int(input()))

num.sort()

for i in range(len(num)) : print(num[i])