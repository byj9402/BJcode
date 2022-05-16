import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
x = int(input())
num.sort()

cnt = 0
left, right = 0, N-1

while left < right :
    if num[left] + num[right] > x : right -= 1
    elif num[left] + num[right] < x : left += 1
    else :
        cnt += 1
        left += 1

print(cnt)