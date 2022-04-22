import sys

S = input()

card = [0] * (10 ** 7)
card[0] = int(S[0])
cnt = 0

for i in range(1, len(S)) :
    card[i] = int(S[i])
    if card[i] != card[i - 1] :
        cnt += 1

if cnt % 2 == 0 : print(cnt // 2)
else : print(cnt // 2 + 1)