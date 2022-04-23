T = int(input())

# T번 만큼 반복
for _ in range(0, T) :
    S = input()
    result = 0
    grade = 0
    
    #점수 계산
    for i in range(0, len(S)) :
        if i == 0 and S[i] == 'O' :
            grade = 1
            result += grade
        if i > 0 and S[i] == 'O' :
            if S[i - 1] == 'O' :
                grade += 1
                result += grade
            else :
                grade = 1
                result += grade
            
    print(result)