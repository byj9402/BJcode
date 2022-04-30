import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N) :
    command = input().split()

    if command[0] == 'push_front' : stack.insert(0, command[1])
    elif command[0] == 'push_back' : stack.append(command[1])
    elif command[0] == 'size' : print(len(stack))
    elif command[0] == 'pop_front' :
        if len(stack) != 0 :
            print(stack[0])
            del stack[0]
        else : print('-1')
    elif command[0] == 'pop_back' :
        if len(stack) != 0 :
            print(stack[len(stack) - 1])
            del stack[len(stack) - 1]
        else : print('-1')
    elif command[0] == 'empty' :
        if len(stack) != 0 : print('0')
        else : print('1')
    elif command[0] == 'front' :
        if len(stack) != 0 : print(stack[0])
        else : print('-1')
    elif command[0] == 'back' :
        if len(stack) != 0 : print(stack[len(stack) - 1])
        else : print('-1')