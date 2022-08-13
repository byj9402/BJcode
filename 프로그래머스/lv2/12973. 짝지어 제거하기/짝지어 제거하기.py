from collections import deque

def solution(s):
    queue = deque(s)
    temp = []
    
    while (queue) :
        a = queue.popleft()
        if len(temp) != 0 :
            if temp[-1] == a : temp.pop()
            else : temp.append(a)
        else : temp.append(a)
            
    if len(temp) == 0 : answer = 1
    else : answer = 0
    
    return answer