import sys
input = sys.stdin.readline

N, L = map(int, input().split())

for temp in range(L, 101) :

    result = []
    num = int((2*N-temp*temp+temp) * (2*temp) ** (-1))

    if num < 0 : num = 0
    
    for i in range(num, num + temp) :
        result.append(i)

    if sum(result) == N :
        print(' '.join(map(str, result)))
        break
    else :
        if temp == 100 : print('-1')