# 완탐 DFS

def solution(numbers, target):
    buho = [1,-1]
    answer = 0
    
    def dfs(idx, current):
        nonlocal answer
        #print(current)
        if idx == len(numbers):
            if current == target:
                answer += 1
            return
        
        for b in buho:
            dfs(idx+1, current + numbers[idx]*b)
        
    dfs(0,0)
    
    return answer