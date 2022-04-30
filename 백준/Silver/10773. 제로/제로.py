import sys
input = sys.stdin.readline

accont = []
K = int(input())
for _ in range(K) :
    money = int(input())
    if money == 0 :
        del accont[len(accont) - 1]
    else : accont.append(money)

print(sum(accont))