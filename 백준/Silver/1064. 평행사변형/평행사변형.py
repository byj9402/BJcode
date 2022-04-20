import sys
import math
input = sys.stdin.readline

Xa, Ya, Xb, Yb, Xc, Yc = map(float, input().split())

# 각 세 점이 일직선 상에 있는 지 확인
# 일직선상에 있을 경우 평행사변형을 만들 수 없음
if ((Ya - Yb) * (Xa - Xc) == (Ya - Yc) * (Xa - Xb))  :
    print("-1.0")
else :
    AB = ((Xa - Xb) ** 2 + (Ya - Yb) ** 2) ** 0.5
    BC = ((Xb - Xc) ** 2 + (Yb - Yc) ** 2) ** 0.5
    CA = ((Xc - Xa) ** 2 + (Yc - Ya) ** 2) ** 0.5
    
    if (BC > AB and BC > CA) : big = BC
    elif (AB > BC and AB > CA) : big = AB
    else : big = CA
        
    if (BC < AB and BC < CA) : small = BC
    elif (AB < BC and AB < CA) : small = AB
    else : small = CA
        
    print((big-small) * 2)