import sys
sys.setrecursionlimit(10**6)

def fact(num) :
    if num <= 1 :
        return 1
    return num * fact(num-1)

t = int(input())

for _ in range (0, t) :
    N = int(input())
    N_fact = fact(N)
    N_str = str(N_fact)
    N_len = len(N_str)

    for i in range (0, N_len) :
        if N_fact % 10 != 0 :
            break
        else :
            N_fact = N_fact // 10

    N_str = str(N_fact)

    print(N_str[len(N_str)-1:])