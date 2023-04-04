import sys
input = sys.stdin.readline

N, M = map(int,input().split())
while (N%M>0) :
    K = N%M
    N = M
    M = K
for i in range (M) :
    print("1", end="")
print("\n")