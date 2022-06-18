import sys
input = sys.stdin.readline

FF, FS, SF, SS = map(int, input().split())
sound = 0

if SF + FS == 0 :
    if FF == 0 : sound = SS
    else : sound = FF
elif FF + FS == 0 : sound = SS + 1
elif SF + SS == 0 : sound = FF + 1
else :
    sound = FF
    if FS != 0 :
        if FS > SF : 
            sound += SF * 2 + 1
            sound += SS
        else :
            sound += FS * 2
            sound += SS

print(sound)