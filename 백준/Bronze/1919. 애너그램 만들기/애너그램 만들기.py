first = input()
second = input()

alpha = list(set(first+second))
temp = [[0, 0] for i in range(len(alpha))]

for i in range(len(alpha)) :
    temp[i][0] = first.count(alpha[i])
    temp[i][1] = second.count(alpha[i])

result = 0
for i in range(len(temp)) :
    if temp[i][0] - temp[i][1] < 0 :
        result += temp[i][1] - temp[i][0]
    elif temp[i][0] - temp[i][1] > 0 :
        result += temp[i][0] - temp[i][1]

print(result)