def pelin(n) :
    nStr = list(n)
    nReverse = list(reversed(n))
    if nStr == nReverse : return True
    else : return False

S = input()
while (S != '0') :
    if pelin(S) : print('yes')
    else : print('no')
    S = input()