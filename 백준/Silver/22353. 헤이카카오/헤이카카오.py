import sys
input = sys.stdin.readline

a, d, k = map(int, input().split())

def expected(d):
    if d >= 100: return a
    result = d * 0.01 * a + (100-d) * 0.01 * (a + expected(d * (1 + k * 0.01)))
    return result

print("{:.10f}".format(expected(d)))