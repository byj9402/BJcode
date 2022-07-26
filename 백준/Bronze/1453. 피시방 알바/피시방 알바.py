import sys
input = sys.stdin.readline

N = int(input())
count = 0
Guest = list(map(int, input().split()))
rejected = []

for a in Guest :
    if a not in rejected :
        rejected.append(a)
    else : 
        count += 1

print(count)