N = input()
num = [0] * len(N)
sum = 0

for i in range(0, len(N)) :
    num[i] = int(N[i])
    sum += num[i]

num.sort(reverse = True)

if sum % 3 == 0 and num[len(num)-1] == 0 :
    for i in range(0, len(num)) : print(num[i], end='')
else : print(-1)