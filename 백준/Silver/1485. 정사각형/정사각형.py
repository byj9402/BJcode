import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    result = False
    rectangle = []
    line = []
    for _ in range(4) :
        rectangle.append(list(map(int, input().split())))
    line = [((rectangle[0][0] - rectangle[1][0]) ** 2 + (rectangle[0][1] - rectangle[1][1]) ** 2),
        ((rectangle[0][0] - rectangle[2][0]) ** 2 + (rectangle[0][1] - rectangle[2][1]) ** 2),
        ((rectangle[0][0] - rectangle[3][0]) ** 2 + (rectangle[0][1] - rectangle[3][1]) ** 2),
        ((rectangle[1][0] - rectangle[2][0]) ** 2 + (rectangle[1][1] - rectangle[2][1]) ** 2),
        ((rectangle[1][0] - rectangle[3][0]) ** 2 + (rectangle[1][1] - rectangle[3][1]) ** 2),
        ((rectangle[2][0] - rectangle[3][0]) ** 2 + (rectangle[2][1] - rectangle[3][1]) ** 2)]
    line.sort()
    if line[0] == line[1] == line[2] == line[3] :
        if line[4] == line[5] :
            if line[0] + line[1] == line[5]: result = True
    if not result : print(0)
    else : print(1)