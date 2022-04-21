import sys
input = sys.stdin.readline

N = int(input())
t = list(map(int, input().split()))

t.sort(reverse = True)
maxDay = 0

#나무를 심고 자라는 데까지 걸리는 시간
for i in range (0, N) :
    day = t[i] + i + 1
    if day > maxDay :
        maxDay = day

#이장님을 초대하게 되는 날짜
maxDay += 1

print(maxDay)