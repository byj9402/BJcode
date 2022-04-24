def sqrtNoNoNum(minN, maxN) :
    for i in range(2, int(maxN ** 0.5) + 1) :
        n = i ** 2 - minN % (i**2)
        if n == i ** 2 :
            n = 0
        while n <= (maxNum - minNum) :
            if cnt[n] : cnt[n] = False
            n += i ** 2
 
minNum, maxNum = map(int, input().split())
cnt = [True] * (maxNum - minNum + 1)

sqrtNoNoNum(minNum, maxNum)
count = 0

for i in cnt :
    if i is True : count += 1
    
print(count)