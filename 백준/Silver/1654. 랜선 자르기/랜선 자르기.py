import sys
input = sys.stdin.readline

## 입력받기
N, M = map(int, input().split())
cable = [int(input()) for _ in range(N)]

## cable을 분할할 길이를 구하기 위해
## 이분탐색을 하기 위한 start/end 정하기
start, end = 1, max(cable)

## 이분 탐색
## count = cable을 분할한 개수
## start가 end보다 작아지는 순간
## end == mid
## >> count가 M과 같고 end값이 가장 큰 경우
while start <= end :
    result = (start + end) // 2
    count = 0
    for line in cable :
        count += line // result
    
    ## 지정된 개수보다 클 때
    if count >= M :
        start = result + 1
    ## 지정된 개수보다 작을 때
    else :
        end = result - 1

print(end)