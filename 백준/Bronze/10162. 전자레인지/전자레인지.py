A = 300
B = 60
C = 10

time = int(input())

A = time // A
time -= A * 300
B = time // B
time -= B * 60
C = time // C
time -= C * 10

if time != 0 : print(-1)
else : print(A, B, C)