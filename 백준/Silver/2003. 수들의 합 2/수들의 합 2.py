import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right <= N and left <= right :
    target = sum(num[left:right])
    if target == M :
        cnt += 1
        right += 1
    elif target < M : right += 1
    else : left += 1
print(cnt)