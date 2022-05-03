import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

#start에서 end까지 펠린드롬인지 판별하기 위한 list
palindrome = [[0] * N for _ in range(N)]

for i in range(N) :
    for start in range(N - i) :
        end = start + i
        if start == end : palindrome[start][end] = 1
        elif num[start] == num[end] :
            if end - start == 1 : palindrome[start][end] = 1
            elif palindrome[start + 1][end - 1] == 1 : palindrome[start][end] = 1

for _ in range(int(input())) :
    S, E = map(int, input().split())
    #list의 번호 + 1 = S, E로 주어지는 값
    print(palindrome[S - 1][E - 1])