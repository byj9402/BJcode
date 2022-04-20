from typing import Counter
import sys
input = sys.stdin.readline

N = int(input())
num = [int(input()) for _ in range(N)]
num.sort()

sum = 0
for i in range(N) :
    sum = sum + num[i]
mean = round(sum/(len(num)))
print(mean)

middle = N // 2
print(num[middle])

num_s = Counter(num).most_common()
if len(num_s) > 1:
    if num_s[0][1] == num_s[1][1]:
        print(num_s[1][0])
    else:
        print(num_s[0][0])
else:
    print(num_s[0][0])

print(num[N-1]-num[0])