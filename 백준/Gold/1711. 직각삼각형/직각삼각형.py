import sys
input = sys.stdin.readline

N = int(input())

dots = []
for _ in range(N) :
    dots.append(tuple(list(map(int, input().split()))))

result = 0
for i in range(N-2) :
    for j in range(i+1, N-1) :
        for k in range(j+1, N) :
            A, B, C = dots[i], dots[j], dots[k]
            a = (A[0]-B[0])**2 + (A[1]-B[1])**2
            b = (B[0]-C[0])**2 + (B[1]-C[1])**2
            c = (A[0]-C[0])**2 + (A[1]-C[1])**2
            if max(a, b, c) * 2 == a + b + c : result += 1

print(result)