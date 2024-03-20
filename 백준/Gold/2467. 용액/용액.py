import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int, input().split()))
solution = sorted(solution, key= lambda x : abs(x), reverse=True)

max_num = 2000000000
result = []

for i in range(1, N) :
    s1, s2 = solution[i-1], solution[i]
    temp = abs(s1+s2)
    if max_num >= temp :
        result.append([temp, s1, s2])
        max_num = temp

result = sorted(result, key= lambda x : x[0])
print(min(result[0][1], result[0][2]), max(result[0][1], result[0][2]))