import sys
input = sys.stdin.readline

N = list(map(str,input().strip()))
number = [0] * 9
for i in range(len(N)) :
    N[i] = int(N[i])
for x in N :
    if x == 6 or x == 9 : number[6] += 1
    else : number[x] += 1

if number[6] % 2 == 0 : number[6] //= 2
else : number[6] = number[6] // 2 + 1
print(max(number))