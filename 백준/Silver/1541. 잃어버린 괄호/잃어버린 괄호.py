import sys
input = sys.stdin.readline

# -를 기준으로 괄호를 넣어주면 최솟값이 된다
S = list(map(str, input().rstrip().split('-')))
min = 0

# +연산자가 끼어있을 경우 식을 리스트로 나누어 계산한다
for i in range(len(S)) : S[i] = list(map(str, S[i].split('+')))

# 수는 0으로 시작될 수 없다
# 따라서 0으로 시작할 경우 0으로 바꾸어 숫자가 아닌 것으로 취급한다
for i in range(len(S)) :
    if S[i][0] == '0' : S[i] = 0

if S[0] != 0 :
    n = 0
    for i in range(len(S[0])) : n += int(S[0][i])
    min += n

for i in range(1, len(S)) : 
    m = 0
    for j in range(len(S[i])) : m += int(S[i][j])
    if S[i] != 0 : min -= m

print(min)