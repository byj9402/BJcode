num = int(input())
word = list('SciComLove')
result = word[num:10] + word[0:num]
print(''.join(result))