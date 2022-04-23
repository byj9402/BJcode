N = int(input())
heightAndWeight = [0,0] * N

for i in range(0, N) : heightAndWeight[i] = list(map(int, input().split()))
    
for i in range(0, N) :
    cnt = 1
    for j in range(0, N) :
        if heightAndWeight[i][0] < heightAndWeight[j][0] \
        and heightAndWeight[i][1] < heightAndWeight[j][1] : cnt += 1
    print(cnt, end = ' ')