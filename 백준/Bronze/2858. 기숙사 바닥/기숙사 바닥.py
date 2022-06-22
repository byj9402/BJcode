import sys
input = sys.stdin.readline

R, B = map(int, input().split())
num = []
max = int((R+B) ** 0.5)

for i in range(3, max + 1) :
    num.append([(R+B) // i, i])

for i in range(len(num)) :
    tempRed = (num[i][0] + num[i][1]) * 2 - 4
    tempBrown = (num[i][0] - 2) * (num[i][1] - 2)
    if tempRed == R and tempBrown == B :
        print(*num[i])
        break