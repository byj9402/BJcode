import sys
input = sys.stdin.readline

n = int(input())
pizza = list(map(str, input().split()))

result = 0

pizza = list(set(pizza))
for i in range(len(pizza)) :
    if pizza[i][-6:] == 'Cheese' :
        result += 1

print('yummy' if result >= 4 else 'sad')