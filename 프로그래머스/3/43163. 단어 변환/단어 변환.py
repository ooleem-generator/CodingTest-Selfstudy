from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    words.append(begin)
    
    length = len(words)
    
    graph = [[] for _ in range(length)]
    visited = [False]*(length)
    
    for i in range(length-1):
        for j in range(i+1, length):
            count = 0
            for a,b in zip(words[i],words[j]):
                if a != b:
                    count += 1
            if count == 1:
                graph[i].append(j)
                graph[j].append(i)
            #print(count)
    
    print(graph)
    
    queue = deque()
    queue.append(length-1)
    visited[length-1] = True
    count = 0
    
    while queue:
        for _ in range(len(queue)):
            i = queue.popleft()
            if words[i] == target:
                return count
            for j in graph[i]:
                if not visited[j]:
                    visited[j] = True
                    queue.append(j)
        count += 1
    
    
    return count