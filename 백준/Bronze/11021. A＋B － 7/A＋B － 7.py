import sys
input = sys.stdin.readline

for i in range(int(input())) :
    x, y = map(int, input().split())
    print("Case #{}: {}".format(i+1, x+y))