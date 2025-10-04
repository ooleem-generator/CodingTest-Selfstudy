def solution(clothes):
    clothes_hash = {}
    cloth_type = set()
    for cloth in clothes:
        #clothes_hash[cloth[0]] = cloth[1]
        if cloth[1] not in clothes_hash:
            clothes_hash[cloth[1]] = [cloth[0]]
        else:
            clothes_hash.get(cloth[1]).append(cloth[0])
    
    cloth_number = list(map(len, list(clothes_hash.values())))
    answer = 1
    for i in cloth_number:
        answer *= (i+1)
    
    return answer-1