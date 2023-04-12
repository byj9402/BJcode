import sys
input = sys.stdin.readline

student = []
N = int(input())
for _ in range(N) :
    tmp = list(map(str, input().split()))
    age = int(tmp[3])*365 + int(tmp[2])*30 + int(tmp[1])
    student.append([tmp[0],age])

student.sort(key = lambda x : x[1],reverse=True)

print(student[0][0])
print(student[-1][0])