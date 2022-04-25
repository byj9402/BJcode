score = [int(input()) for _ in range(8)]
scoreSort = sorted(score, reverse=True)
scoreSum = sum(scoreSort[:5])
scoreIndex = sorted([score.index(scoreSort[i])+1 for i in range(5)])
print(scoreSum)
print(*scoreIndex)