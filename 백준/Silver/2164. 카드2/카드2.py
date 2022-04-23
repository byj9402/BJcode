num = int(input())

if num == 1 : print(num)
else :
    result = 1
    while(result < num) : result *= 2
    if result == num : print(num)
    else :
        result //= 2
        num -= result
        num *= 2
        print(num)