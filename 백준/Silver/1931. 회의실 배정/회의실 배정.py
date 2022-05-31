import sys
input = sys.stdin.readline

N = int(input())
meeting = []

for _ in range(N) :
    meeting.append(list(map(int, input().split())))
    
### loop를 한번만 쓸 수 있게 정렬
### [0] 정렬 후 [1] 기준으로 정렬
### 가장 빨리 시작해서 가장 일찍 끝나게 할 수 있음
meeting.sort(key = lambda x : x[0])
meeting.sort(key = lambda x : x[1])

cnt = 0
h = 0

for i in range(N) :
    if meeting[i][0] >= h :
        cnt += 1
        h = meeting[i][1]
    
print(cnt)