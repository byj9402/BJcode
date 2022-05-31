import sys
input = sys.stdin.readline

K = int(input())
A = 1
B = 0

for _ in range(K) :
    originA = A
    originB = B
    A = A + originB - originA
    B = B + originA

print(A, B)