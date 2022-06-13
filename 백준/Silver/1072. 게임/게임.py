from math import floor
import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = Y * 100 // X
low, high = 0, X
if Z >= 99 : high = -2
else :
    while(low <= high) :
        mid = (low + high) // 2
        tx, ty = X + mid, Y + mid
        if floor(100 * ty // tx) > floor(100 * Y // X): high = mid - 1
        else: low = mid + 1

print(high+1)