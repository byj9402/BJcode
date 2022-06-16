import sys
input = sys.stdin.readline

A, B = map(int, input().split())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

print(len(set(num1 + num2)) * 2 - len(num1) - len(num2))