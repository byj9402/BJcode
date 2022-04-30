from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))
cardSum = []

for cards in combinations(card, 3) : cardSum.append(sum(cards))
cardSum.sort(reverse = True)

for i in range(len(cardSum)) :
    if cardSum[i] <= M : 
        print(cardSum[i])
        break