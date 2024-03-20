import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    num = list(map(int,input().split()))
    num.sort(reverse = True)
    print(num[2])