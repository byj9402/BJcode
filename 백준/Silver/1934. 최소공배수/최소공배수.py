import sys
input = sys.stdin.readline

#최대공약수
def gcd(x, y):
  if y == 0:
    return x
  else:
    return gcd(y, x%y)

#최소공배수
def lcm(x, y):
  result = (x*y) // gcd(x,y)
  return result

num = int(input())

for i in range(num):
  x, y = map(int, input().split())
  print(lcm(x, y))