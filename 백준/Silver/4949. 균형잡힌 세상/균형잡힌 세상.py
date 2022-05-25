import sys
input = sys.stdin.readline

while (True) :
    stack = []
    line = input().rstrip()
    if line == '.' : break
    for x in line : 
        if x == '[' or x == '(' : stack.append(x)
        elif x == ']' :
            if len(stack) != 0 and stack[-1] == '[' : stack.pop()
            else :
                stack.append(']')
                break
        elif x == ')' :
            if len(stack) != 0 and stack[-1] == '(' : stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 : print('yes')
    else : print('no')