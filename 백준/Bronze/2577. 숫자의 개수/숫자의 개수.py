A = int(input())
B = int(input())
C = int(input())
mult = A * B * C
num = list(map(int, str(mult)))

cnt = [0] * 10

for i in range(0, len(num)) :
    j = int(num[i])
    cnt[j] += 1

for i in range(0, 10) : print(cnt[i])