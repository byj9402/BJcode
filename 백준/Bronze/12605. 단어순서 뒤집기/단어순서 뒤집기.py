L = []
N = int(input())
for i in range(N) : L.append(input().split(' '))
for i in range(N) :
    num = i + 1
    L[i].reverse()
    print(f"Case #{num}:", end = ' ')
    print(*L[i])