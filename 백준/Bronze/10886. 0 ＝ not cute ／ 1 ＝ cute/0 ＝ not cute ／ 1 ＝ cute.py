import sys
input = sys.stdin.readline

CUTE = 0
nope = 0

for _ in range(int(input())) :
    x = int(input())
    if x == 1 : CUTE += 1
    else : nope += 1

if CUTE < nope : print("Junhee is not cute!")
else : print("Junhee is cute!")