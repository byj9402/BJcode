import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))

i, j = 0, 0

## 결과값을 저장할 변수
temp = 0
## 길이를 저장할 list
result = []

while(True) :
    if temp >= S :
        result.append(j - i)
        temp -= num[i]
        i += 1
    else :
        if j == N : break
        temp += num[j]
        j += 1

if len(result) == 0 : print(0)
else : print(min(result))