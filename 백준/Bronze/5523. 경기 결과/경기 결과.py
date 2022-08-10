import sys

a = b = 0
for _ in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    if A > B:
        a += 1
    elif A < B:
        b += 1
print(a, b)