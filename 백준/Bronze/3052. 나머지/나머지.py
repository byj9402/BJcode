div = [0] * 10
cnt = 1

for i in range(0, 10) :
    n = int(input())
    div[i] = n % 42

divSet = list(set(div))

print(len(divSet))