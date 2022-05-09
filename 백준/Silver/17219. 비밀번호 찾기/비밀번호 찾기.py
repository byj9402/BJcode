import sys
input = sys.stdin.readline

N, M = map(int, input().split())
password = {}

for _ in range(N) :
    site, pw = input().split()
    password[site] = pw

for _ in range(M) : print(password[input().strip()])