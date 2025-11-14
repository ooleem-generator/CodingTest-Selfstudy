def solution(n, s):
    answer = []
    if s//n == 0:
        answer.append(-1)
    else:
        m, remainder = divmod(s, n)
        for _ in range(n-remainder):
            answer.append(m)
        for _ in range(remainder):
            answer.append(m+1)
        
    
    return answer