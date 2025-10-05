def dfs(graph, v, visited):
    visited[v] = True # 이거 까먹으면 안되지
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def solution(n, computers):
    
    visited = [False]*(n+1)
    visited[0] = True # 뒤의 while문 조건을 위해
    
    graph = [[] for _ in range(n+1)]
    for i, v in enumerate(computers):
        for j in range(n):
            if i != j and v[j] == 1:
                graph[j+1].append(i+1)
    
    count = 0
    
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1
    
    return count