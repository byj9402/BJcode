import sys
input = sys.stdin.readline

N = int(input())
print((N // 5)+(N // (5**2))+(N // (5**3)))