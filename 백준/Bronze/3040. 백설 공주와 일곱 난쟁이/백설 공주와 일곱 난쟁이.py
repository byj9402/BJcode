dwarf = [int(input()) for _ in range(9)]
answer = False

for i in range(9) :
    for j in range(9) :
        if dwarf[i] + dwarf[j] == sum(dwarf) - 100 :
            if i != j :
                result = [i, j]
                answer = True
                break
    if answer : break

for k in range(9) :
    if k not in result :
        print(dwarf[k])