line1, line2 = input(), input()
length = [[0] * (len(line2) + 1) for _ in range(len(line1) + 1)]
result = 0

for i in range(len(line1)) :
    for j in range(len(line2)) :
        if line1[i] == line2[j] :
            length[i][j] = length[i-1][j-1] + 1
            result = max(length[i][j], result)

print(result)