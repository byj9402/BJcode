import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
work = list(map(int, input().split()))
work.sort()

four = False

# 7의 배수일 경우 의미가 없음
for i in range(1, (100000//7) + 1) :
    seven = i * 7
    while seven in work : work.remove(seven)

# 할 일이 5개 이상일 경우
# 7로 나누었을 때 4를 도출할 수 있음
if len(work) > 5 : four = True
elif sum(work) % 7 == 4 : four = True
else :
    num = []
    # 4로 나누어지는 수가 하나라도 있으면
    # 금요일에 정확히 일을 끝마칠 수 있음
    for i in range(len(work)) :
        if work[i] % 7 == 4 :
            four = True
            break
    # 그 외 조합
    for i in range(1, len(work)) :
        for j in list(combinations(work, i)) :
            num.append(j)
    num = list(set(num))
    for i in range(len(num)) :
        num[i] = list(num[i])
        result = 0
        for j in range(len(num[i])) :
            result += int(num[i][j])
        if result % 7 == 4 :
            four = True
            break

if not four : print('NO')
else : print('YES')