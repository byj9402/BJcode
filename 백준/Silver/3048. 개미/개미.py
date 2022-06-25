import sys
input = sys.stdin.readline

N1, N2 = map(int, input().split())
ant1 = (list(map(str, input().strip())))
ant2 = list(map(str, input().strip()))

ant1.reverse()
load = ant1 + ant2

for _ in range(int(input())) :
    for i in range(len(load) - 1) :
        if load[i] in ant1 and load[i + 1] in ant2 :
            load[i], load[i + 1] = load[i + 1], load[i]
            if load[i + 1] == ant1[-1] : break

print("".join(load))