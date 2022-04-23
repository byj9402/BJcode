s = list(input())
saveAlpha = 'abcdefghijklmnopqrstuvwxyz'

for x in saveAlpha :
    if x in s : print(s.index(x), end = " ")
    else : print('-1', end = " ")
print()