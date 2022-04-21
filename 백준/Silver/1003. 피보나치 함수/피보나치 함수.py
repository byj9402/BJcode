fib = [0] * 40

def fibonacci(n) :
    if n == 0 : return 1
    if n == 1 : return 1
    if fib[n] != 0 :
        return fib[n]
    fib[n] = fibonacci(n-1) + fibonacci(n-2)
    return fib[n]

t = int(input())

for i in range(0, t) :
    N = int(input())
    if N == 0 : print('1 0')
    elif N == 1 : print('0 1')
    else : print(fibonacci(N-2), fibonacci(N-1))