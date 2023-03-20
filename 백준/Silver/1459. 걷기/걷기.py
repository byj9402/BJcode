import sys
input = sys.stdin.readline

X, Y, W, S = map(int, input().split())
temp1 = (X + Y) * W
temp2 = max(X, Y) * S if (X + Y) % 2 == 0 else (max(X, Y) - 1) * S + W
temp3 = (min(X, Y) * S) + abs(X - Y) * W

print(min(temp1, temp2, temp3))