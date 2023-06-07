import sys
input = sys.stdin.readline

## 최대공약수 구하는 함수
def gcd(a, b) :
    n = 1
    if a < b : a, b = b, a
    while(b != 0) :
        n = a%b
        a = b
        b = n
    return a

# ## 1~a까지 모두 더하는 함수
# def add_all(a) :
#     return (a*(a+1))//2

# T = int(input())

# for _ in range(T) :

#     result = 0
#     p, q, n = map(int, input().split())

#     ## 최대공약수 구하기
#     GCD = gcd(p, q)

#     ## 서로소로 만들기
#     p //= GCD
#     q //= GCD

#     ## p가 q보다 클 때
#     if p > q :
#         result += ((n//q)*add_all(q-1))
#         if n%q != 0 :
#             ## 홀수+홀수 / 짝수+짝수일 경우 역순 증가
#             if p%2 != q%2 :
#                 result += (add_all(q-1) - add_all(q-1-(n%q)))
#             ## 홀수+짝수 / 짝수+홀수일 경우 순차적 증가    
#             else :
#                 result += (add_all(n%q))
#         print(result * GCD)
        
#     ## p가 q보다 작을 때
#     elif p < q :
#         result += ((n//q)*add_all(q-1))
#         if n%q != 0 :
#             ## 홀수+홀수 / 짝수+짝수일 경우 역순 증가
#             if p%2 != q%2 :
#                 result += 0
#             ## 홀수+짝수 / 짝수+홀수일 경우 순차적 증가
#             else :
#                 result += 0
#         print(result * GCD)

#     ## p과 q가 같을 때
#     else : 
#         print(0)


def div_sum(p, q , n) :
    if n == 0 or q == 0 : return 0
    if q == 1 : return p*n*(n+1) // 2
    if p > q : return div_sum(p%q, q, n) + n*(n+1) // 2*(p//q)
    return n*(n*p//q) + (n//q) - div_sum(q, p, n*p//q)

def mod_sum(p, q, n) :
    GCD = gcd(p, q)
    return p*n*(n+1)//2 - q*div_sum(p//GCD, q//GCD, n)

for _ in range(int(input())) :
    p, q, n = map(int, input().split())
    print(mod_sum(p, q, n))