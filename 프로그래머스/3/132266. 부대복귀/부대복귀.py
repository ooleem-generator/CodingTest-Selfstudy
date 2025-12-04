from heapq import heappush, heappop

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    
    for i, j in roads:
        graph[i].append(j)
        graph[j].append(i)
    
    shortest = [10**15]*(n+1)
    
    def dijkstra(start):
        #nonlocal shortest
        queue = []
        heappush(queue, [0, start])
        shortest[start] = 0
        while queue:
            accum_dist, curr_node = heappop(queue)
            for next_node in graph[curr_node]:
                if accum_dist + 1 >= shortest[next_node]:
                    continue
                shortest[next_node] = accum_dist + 1
                heappush(queue, [accum_dist+1, next_node])
        
        #return shortest[destination] if shortest[destination] != 10**15 else -1
    
    dijkstra(destination)
    
    answer = []
    
    for i in sources:
        if shortest[i] == 10**15:
            answer.append(-1)
        else:
            answer.append(shortest[i])
    
    return answer