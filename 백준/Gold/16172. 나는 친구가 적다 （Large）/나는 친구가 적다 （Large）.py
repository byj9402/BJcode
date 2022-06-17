S = input()
K = input()

for i in range(10) : S = S.replace(str(i), '')

if K in S : print(1)
else : print(0)