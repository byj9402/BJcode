import sys
input = sys.stdin.readline

x = int(input())
y = int(input())
if x < 0 : print(3) if y < 0 else print(2)
else : print(4) if y < 0 else print(1)