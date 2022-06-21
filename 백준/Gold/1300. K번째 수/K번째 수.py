import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

def binary(start, end, k) :
    while (start <= end) :
        mid = (start + end) // 2
        temp = 0
        for i in range(1, N + 1) :
            temp += min(mid // i, N)

        if temp >= k :
            end = mid - 1
        else :
            start = mid + 1
    return start

print(binary(1, N * N, k))