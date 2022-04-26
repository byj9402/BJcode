N = int(input())
stair = [int(input()) for _ in range(N)]

if N == 1 : print(stair[0])
elif 1 < N < 3 : print(stair[0] + stair[N-1])
else :
    stairSum = []
    stairSum.append(stair[0])   #stairSum[0]
    stairSum.append(max(stair[0] + stair[1], stair[1])) #stairSum[1]
    stairSum.append(max(stair[0] + stair[2], stair[1] + stair[2]))  #stairSum[2]

    for i in range(3, N) :
        stairSum.append(max(stairSum[i - 2] + stair[i], stairSum[i - 3] + stair[i] + stair[i - 1]))

    print(stairSum[-1])