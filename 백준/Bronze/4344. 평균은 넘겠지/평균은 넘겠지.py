import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    num = list(map(int, input().split()))
    mean = sum(num[1:]) / num[0]
    
    cnt = 0
    for i in range(1, num[0] + 1) :
        if mean < num[i] : cnt += 1

    smart = (cnt / num[0]) * 100
    print("{:.3f}%" .format(smart))