import sys
input = sys.stdin.readline

num = input().strip()

for i in range(1, len(num)+1):
    num2 = num[:i]
    n = int(num2)

    while len(num2) < len(num):
        n += 1
        num2 += str(n)
  
    if num2 == num: break

print(num[:i], n)