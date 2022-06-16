import sys
input = sys.stdin.readline

for i in range(int(input())) :
    x, y = map(int, input().split())
    print("Case #{0}: {1} + {2} = {3}".format(i+1, x, y, x+y))