import sys
input = sys.stdin.readline

line = input().strip()
bomb = list(input().strip())
power = len(bomb)
stack = []

for x in line : 
    stack.append(x)
    if stack[-power:] == bomb :
        for _ in range(power) : stack.pop()

if len(stack) == 0 : print("FRULA")
else : print(*stack, sep='')