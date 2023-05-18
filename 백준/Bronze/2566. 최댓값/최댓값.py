import sys
input = sys.stdin.readline

field = []
for _ in range(9) :
    field.append(list(map(int, input().split())))

# max 구하기 & max 값이 있는 열 저장
max_num = 0
max_line = 0
for i in range(9) :
    if max(field[i]) > max_num :
        max_num = max(field[i])
        max_line = i

# max_num의 index 구하기
max_index = field[max_line].index(max_num)

print(max_num)
print(max_line+1, max_index+1)