import math

n = int(input())
nFact = str(math.factorial(n))
for i in nFact[::-1]:
    if i == '0': continue
    else:
        print(i)
        break