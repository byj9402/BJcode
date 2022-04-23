def maxDiv(a, b) :
    while (a % b != 0) :
        a, b = b, a % b
    return b

def minMult(a, b, div) :
    return int(a * b // div)

A, B = map(int, input().split())
maxDiv = maxDiv(A, B)
print(maxDiv)
print(minMult(A, B, maxDiv))