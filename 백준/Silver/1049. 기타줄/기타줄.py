import sys
input = sys.stdin.readline

N, M = map(int, input().split())
package = []
single = []

for _ in range(M) :
    x, y = map(int, input().split())
    package.append(x)
    single.append(y)

package.sort()
single.sort()

money = []

for i in range((N // 6) + 1) : money.append(package[0] * i + single[0] * (N - 6 * i))
money.append(package[0] * (N // 6 + 1))

print(min(money))