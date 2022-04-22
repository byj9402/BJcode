import sys

ascending = [i for i in range(1, 9)]
descending = sorted(ascending, reverse = True)

sound = list(map(int, sys.stdin.readline().split()))

if ascending == sound : print('ascending')
elif descending == sound : print('descending')
else : print('mixed')