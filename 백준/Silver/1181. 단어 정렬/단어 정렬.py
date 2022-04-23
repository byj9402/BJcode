import sys

T = int(input())
word = [sys.stdin.readline().strip() for _ in range(0, T)]

word.sort()
word.sort(key = len)

for i in range(0, T) :
    if i == 0 : print(word[i])
    if i > 0 and word[i] != word[i - 1] : print(word[i])