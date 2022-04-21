#int를 reverse해서 출력하는 함수
def printReverse(n) :
    num = list(map(int, str(n)))
    for i in range(0, len(num)) :
        print(num[len(num) - 1 - i], end = '')
    print()

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

if A % 10 > B % 10 : printReverse(A)
elif A % 10 < B % 10 : printReverse(B)
else :
    if A % 100 > B % 100 : printReverse(A)
    elif A % 100 < B % 100 : printReverse(B)
    else :
        if A > B : printReverse(A)
        else : printReverse(B)