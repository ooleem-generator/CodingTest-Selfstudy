def solution(friends, gifts):
    
    convert = {}
    for i, v in enumerate(friends):
        convert[v] = i
    
    gift_log = [{} for _ in range(len(friends))]
    
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i != j:
                gift_log[i][j] = 0
    
    gifts = [[convert[j] for j in i.split(' ')] for i in gifts]
    
    for giver, receiver in gifts:
        gift_log[receiver][giver] += 1
    
    #받은 선물 수
    gift_received = [sum(i.values()) for i in gift_log]    
    #준 선물 수
    gift_gived = [0]*len(friends)
    
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i != j:
                gift_gived[i] += gift_log[j][i]
    
    #선물 지수
    gift_index = [gift_gived[i]-gift_received[i] for i in range(len(friends))]
    
    # 이제 다음 달 계산
    gift_next = [0]*len(friends)
    
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i != j:
                if gift_log[i][j] < gift_log[j][i]:
                    gift_next[i] += 1
                elif gift_log[i][j] == gift_log[j][i]:
                    if gift_index[i] > gift_index[j]:
                        gift_next[i] += 1
    
        
        
    return max(gift_next)