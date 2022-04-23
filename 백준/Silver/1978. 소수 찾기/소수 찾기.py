import sys

def primeNum(n):
    if n == 1: return False
    sq = int(n ** (0.5))
    for i in range(2,sq+1):
        if n % i == 0: return False
    return True

N = int(input())
num = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(0, N) :
    if primeNum(num[i]) is True : cnt += 1
print(cnt)