import sys
sys.setrecursionlimit(10**6)

def solution(n):
    temp = [-1] * (n + 1)
    
    def result(n) :
        if temp[n] != -1 : return temp[n]
        if n == 0 : return 1
        if n == 1 : return 1
        temp[n] = (result(n - 1) + result(n - 2)) % 1000000007
        return temp[n]
    
    return result(n)