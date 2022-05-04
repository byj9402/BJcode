import sys
input = sys.stdin.readline

def binary(array, target, start, end) :
    while start <= end :
        middle = (start + end) // 2
        if array[middle] == target : return 1
        elif array[middle] > target : end = middle - 1
        elif array[middle] < target : start = middle + 1
    return 0

N = int(input())
card = list(map(int, input().split()))
card.sort()

M = int(input())
result = list(map(int, input().split()))
    
for i in range(M) :
    print(binary(card, result[i], 0, N - 1), end = ' ')