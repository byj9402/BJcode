import sys
input = sys.stdin.readline

M = int(input())
stack = []

for _ in range(M) :
    command = input().strip().split(' ')
    if command[0] == 'add' :
        if int(command[1]) not in stack : stack.append(int(command[1]))
    elif command[0] == 'remove' :
        if int(command[1]) in stack : del stack[stack.index(int(command[1]))]
    elif command[0] == 'check' :
        if int(command[1]) in stack : print(1)
        else : print(0)
    elif command[0] == 'toggle' :
        if int(command[1]) not in stack : stack.append(int(command[1]))
        else : del stack[stack.index(int(command[1]))]
    
    if command[0] == 'all' :
        stack = [i for i in range(1, 21)]
    elif command[0] == 'empty' :
        stack.clear()