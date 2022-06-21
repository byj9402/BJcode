import sys
import math
input = sys.stdin.readline

# i가 소수인지 판별하기 위한 함수
def primeNum(n):
    if n == 1:
        return False
    sq = int (math.sqrt(n))
    for i in range(2,sq+1):
        if n % i == 0:
            return False
    return True

p, q = map(int,input().split())

# p가 q보다 클 때를 위해 변환해주는 if문
if(p>q) :
    r = q
    q = p
    p = r

# p에서 q까지의 수가 소수인지 판별하기 위한 loop
for i in range(p,q+1):
    if primeNum(i):
        print(i)