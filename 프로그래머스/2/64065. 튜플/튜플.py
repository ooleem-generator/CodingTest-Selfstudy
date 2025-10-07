def solution(s):
    s = s.replace('},{', ' ').split(' ')
    s[0] = s[0].lstrip('{')
    s[len(s)-1] = s[len(s)-1].rstrip('}')
    s = [list(map(int, t.split(','))) for t in s]
    s.sort(key = lambda x:len(x))
    answer = []
    for i in s:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return answer