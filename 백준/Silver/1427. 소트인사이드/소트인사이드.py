N = input()
num = []
for i in range(len(N)) : num.append(int(N[i]))
num.sort(reverse = True)
print(''.join(map(str,num)))