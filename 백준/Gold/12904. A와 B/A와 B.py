import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

while(True) :
    if len(T) == len(S) : break
    if T[-1] == 'A' :
        del T[-1]
    elif T[-1] == 'B' : 
        del T[-1]
        T.reverse()

if S == T : print(1)
else : print(0)