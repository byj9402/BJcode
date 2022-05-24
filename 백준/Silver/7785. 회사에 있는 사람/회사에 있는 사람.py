import sys
input = sys.stdin.readline

office = {}
for _ in range(int(input())) :
    name, work = map(str, input().strip().split())
    if work == 'enter' : office[name] = 1
    else : del office[name]
office = sorted(office.keys(), reverse = True)
for x in office : print(x)