import sys
input = sys.stdin.readline

T = int(input())
for i in range(T) :
    s = input().rstrip()
    S = list(s)
    VPS = 0
    for x in S:
        if x == '(' : VPS += 1
        elif x == ')' : VPS -= 1
        # ')' 가 '(' 보다 먼저 나와서 닫히지 못할 경우
        if VPS < 0 :
            print('NO')
            break
    if VPS == 0 : print('YES')
    elif VPS > 0 : print('NO')