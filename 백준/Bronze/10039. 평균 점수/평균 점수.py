import sys
input = sys.stdin.readline

grade = []
for _ in range(5) :
    grade.append(int(input()))
for i in range(5) :
    if grade[i] <= 40 : grade[i] = 40
print(sum(grade) // 5)