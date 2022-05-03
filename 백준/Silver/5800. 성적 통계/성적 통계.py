import sys
input = sys.stdin.readline

K = int(input())
Class = []

for _ in range(K) : Class.append(list(map(int, input().split())))

for i in range(K) :
    
    del Class[i][0]
    
    Class[i].sort()
    
    gap = []
    for j in range(1, len(Class[i])) :
        gap.append(Class[i][j] - Class[i][j - 1])

    print('Class', i+1)
    print('Max', max(Class[i]), end = ', ')
    print('Min', min(Class[i]), end = ', ')
    print('Largest gap', max(gap))