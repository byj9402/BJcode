from math import factorial as fact
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
print(fact(n) // (fact(m) * fact(n - m)))