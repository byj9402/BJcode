import sys
input = sys.stdin.readline

def remain(a, b, c) :
    if b == 1 : return a % c
    if b % 2 == 0 : return (remain(a, b//2, c)**2) % c
    else : return ((remain(a, b//2, c)**2) *a) % c

a, b, c = map(int, input().split())
print(remain(a, b, c))