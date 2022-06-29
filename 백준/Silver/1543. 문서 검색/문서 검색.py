import sys
input = sys.stdin.readline

text = input().strip()
word = input().strip()

stack = []
count = 0

for x in text :
    stack.append(x)
    if x == word[-1] :
        if word in "".join(stack) :
            stack = []
            count += 1

print(count)