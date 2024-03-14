import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    N = int(input())
    log = list(map(int, input().split()))

    log = sorted(log)

    result = 0
    for i in range(2, N) :
        result = max(result, log[i] - log[i-2])
    
    print(result)
