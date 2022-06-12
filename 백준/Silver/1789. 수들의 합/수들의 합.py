N = int(input())
n = 1
while (True) :
    if (n * (n + 1) / 2) > N : break
    n += 1
print(n - 1)