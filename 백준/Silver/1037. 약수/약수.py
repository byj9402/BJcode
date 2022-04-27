import sys

N = int(input())
divisor = list(map(int, sys.stdin.readline().split()))
divisor.sort()

if N % 2 != 0 : print(divisor[N // 2] ** 2)
else : print(divisor[0] * divisor[N - 1])