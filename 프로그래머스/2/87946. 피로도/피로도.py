def solution(k, dungeons):
    visited = [False]*len(dungeons)
    dungeons.sort(key=lambda x:-x[0])
    #print(dungeons)
    answer = -1
    
    def dfs(fatigue, visited):
        nonlocal answer
        
        if visited == [True]*len(dungeons):
            answer = len(dungeons)
            return
        
        for i, [limit, consume] in enumerate(dungeons):
            if visited[i] == True or limit > fatigue:
                continue
                
            visited[i] = True
            dfs(fatigue-consume, visited)
            visited[i] = False
            
        else:
            answer = max(answer, visited.count(True))
            return
        
    dfs(k, visited)        
    
    return answer