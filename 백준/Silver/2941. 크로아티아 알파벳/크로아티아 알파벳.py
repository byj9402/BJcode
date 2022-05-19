string = input()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for alpha in croatia :
    if alpha in string :
        string = string.replace(alpha, "0")
print(len(string))