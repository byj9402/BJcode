def solution(answers):
    
    first = [1, 2, 3, 4, 5]                 ## len 5
    second = [2, 1, 2, 3, 2, 4, 2, 5]       ## len 8
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  ## len 10
    
    F_cnt, S_cnt, T_cnt = 0, 0, 0
    
    for i in range(0, len(answers)) :
        if first[i - 5 * (i // 5)] == answers[i] : F_cnt += 1
        if second[i - 8 * (i // 8)] == answers[i] : S_cnt += 1
        if third[i - 10 * (i // 10)] == answers[i] : T_cnt += 1
        
    answer = []
    result = max(F_cnt, S_cnt, T_cnt)
    
    if result == F_cnt : answer.append(1)
    if result == S_cnt : answer.append(2)
    if result == T_cnt : answer.append(3)
    
    return answer