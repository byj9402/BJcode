import sys

N = int(input())
card = list(map(int, sys.stdin.readline().split()))
card.sort()

M = int(input())
num = list(map(int, sys.stdin.readline().split()))

count = {}
for i in card :
    if i in count : count[i] += 1
    else : count[i] = 1

for i in num :
    if count.get(i) == None : print(0, end = ' ')
    else : print(count.get(i), end = ' ')