import sys
input = sys.stdin.readline

line = input().strip()
i = 0

while (True) :
    j = i + 10
    if j > len(line) : j = len(line)
    print(line[i:j])
    i += 10
    if j == len(line) : break