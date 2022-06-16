import sys
input = sys.stdin.readline

A, B = map(int, input().split())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

count = num1 + num2
count = list(set(count))

print(len(count) * 2 - len(num1) - len(num2))