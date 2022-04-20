import sys
impot = sys.stdin.readline
sys.setrecursionlimit(10**6)

def newfact(n) :
    num = 1
    for i in range(1, n+1) :
        num *= i
        while num % 10 == 0 : num = num // 10
    return int(num % 10)

t = int(input())

for _ in range (0,t) :
    N = int(input())
    print(newfact(N))