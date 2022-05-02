import sys
input = sys.stdin.readline

N = int(input())
dic = [0] * 10001

for _ in range(N) : dic[int(input())] += 1
for i in range(len(dic)) :
    for _ in range(dic[i]) : print(i)