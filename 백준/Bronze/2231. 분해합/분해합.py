N = int(input())
minN = N - len(str(N)) * 9

if minN < 0 : minN = 0
for i in range(minN, N) :
    if i + sum(list(map(int, str(i)))) == N :
        print(i)
        break
else : print(0)