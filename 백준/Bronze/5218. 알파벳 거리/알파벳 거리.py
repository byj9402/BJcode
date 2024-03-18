for _ in range(int(input())) :
    result = []
    line1, line2 = map(list, input().split())
    for i in range(len(line1)) :
        temp1 = ord(line1[i])
        temp2 = ord(line2[i])
        if temp2 >= temp1 :
            result.append(temp2 - temp1)
        else :
            result.append(temp2 - temp1 + 26)
    print("Distances:", *result)
    