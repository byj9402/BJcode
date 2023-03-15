import sys
input = sys.stdin.readline

H, W = map(int, input().split())
num = list(map(int, input().split()))

water = 0
for i in range(1, W-1) :
    left = max(num[:i])
    right = max(num[i+1:])
    merge = min(left, right)

    if num[i] < merge :
        water += merge - num[i]

print(water)