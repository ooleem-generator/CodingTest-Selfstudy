supo1 = [1,2,3,4,5]*2000
supo2 = [2,1,2,3,2,4,2,5]*1250
supo3 = [3,3,1,1,2,2,4,4,5,5]*1000

def solution(answers):
    count = [0,0,0]
    for i,v in enumerate(answers): 
        if v == supo1[i]:
            count[0] += 1
        if v == supo2[i]:
            count[1] += 1
        if v == supo3[i]:
            count[2] += 1
    
    count_and_supo = [(i+1, v) for i, v in enumerate(count)]
    max_score = max(count)
    answer = [i[0] for i in count_and_supo if i[1] == max_score]
    answer.sort()
    return answer