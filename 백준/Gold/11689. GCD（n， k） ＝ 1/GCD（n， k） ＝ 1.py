N = int(input())
result = N
for i in range(2, round(N ** 0.5) + 1):
    if N % i == 0:
        while N % i == 0:
            N //= i
        result *= 1 - (1 / i)
if N > 1:
    result *= 1 - (1 / N)
print(round(result))