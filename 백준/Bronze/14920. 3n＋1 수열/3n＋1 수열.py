import sys
input = sys.stdin.readline

n = int(input())
count = 1
while(n != 1) :
    count += 1
    if n % 2 == 1 :
        n = 3 * n + 1
    else :
        n //= 2

print(count)