import sys
input = sys.stdin.readline

N = int(input())
num = list(map(str, input().strip().split()))
result = []

for x in num :
    temp = x
    line = len(temp)
    while len(temp) < 10 :
        temp += temp[len(temp) - line]
    result.append([temp, x])
result.sort(key = lambda x : x[0], reverse = True)

#### 모든 수가 0일 경우 0을 출력
if int(''.join(num)) == 0 : print(0)
else :
    for i in range(N) :
        print(result[i][1], end = '')
    print()