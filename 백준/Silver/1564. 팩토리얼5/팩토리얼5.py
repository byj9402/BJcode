import sys
input = sys.stdin.readline

N = int(input())
result = 1
for i in range(2, N + 1) :
    result *= i
    while (result % 10 == 0) : result //= 10
    result %= 1000000000000

print(f"{str(result)[-5:]}")