import sys
input = sys.stdin.readline

W_university = []
K_university = []

for _ in range(10) :
    W_university.append(int(input()))
for _ in range(10) :
    K_university.append(int(input()))

W_university.sort(reverse=True)
K_university.sort(reverse=True)

print(W_university[0]+W_university[1]+W_university[2],
      K_university[0]+K_university[1]+K_university[2],)