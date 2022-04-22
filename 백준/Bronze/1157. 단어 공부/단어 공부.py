S = input().upper()
alpha = list(set(S))
cntAlpha = []

for x in alpha : cntAlpha.append(S.count(x))
if cntAlpha.count(max(cntAlpha)) >= 2 : print("?")
else : print(alpha[cntAlpha.index(max(cntAlpha))])