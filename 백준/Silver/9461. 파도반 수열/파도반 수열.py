triangle = [0] * 101
triangle[1] , triangle[2], triangle[3], triangle[4] , triangle[5] = [1, 1, 1, 2, 2]
for i in range(6, 101) : triangle[i] = triangle[i - 1] + triangle[i - 5]

for i in range(0, int(input())) : print(triangle[int(input())])