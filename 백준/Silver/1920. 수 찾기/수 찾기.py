import sys

N = int(input())
A = set(map(int, sys.stdin.readline().split()))
M = int(input())
B = list(map(int, sys.stdin.readline().split()))

for i in B : print(1) if i in A else print(0)