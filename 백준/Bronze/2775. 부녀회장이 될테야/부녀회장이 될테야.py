import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    a = int(input())
    b = int(input())
    first = [x for x in range(1, b + 1)]
    for i in range(a) :
        for j in range(1, b) :
            first[j] += first[j - 1]
    print(first[-1])