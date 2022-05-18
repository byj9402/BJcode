import sys
input = sys.stdin.readline

S = input().rstrip().split(":")
if len(S) > 8 and S[0] == '' and S[1] == '' : del S[0]
for i in range(len(S)):
    if len(S[i]) < 4: S[i] = "0" * (4-len(S[i])) + S[i]
if len(S) < 8:
    for i in range(1, len(S)) :
        if S[i] == '' and S[i] == S[i - 1] :
            S[i] = '0000'
            S[i+1] = '0000'
if len(S) < 8:
    for i in range(1, len(S)) :
        if S[i] == '' : S[i] = '0000'
if len(S) < 8 :
    for i in range(1, len(S)) :
        if S[i] == '0000' and S[i - 1] == S[i] :
            for _ in range(i, (8 - len(S)) + i) : S.insert(i + 1, '0000')
if len(S) < 8 :
    for i in range(len(S)) :
        if S[i] == '0000' :
            for _ in range(i, (8 - len(S)) + i) : S.insert(i + 1, '0000')
if len(S) > 8 :
    for i in range(len(S) - 1, 7, -1) :
        del S[i]
print(":".join(S))