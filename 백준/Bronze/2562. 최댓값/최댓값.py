num = [int(input()) for i in range(0, 9)]
numRe = sorted(num, reverse = True)

for i in range(0, len(num)) :
    if num[i] == numRe[0] :
        print(numRe[0], i+1)