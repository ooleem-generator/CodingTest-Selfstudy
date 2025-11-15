# 이건 dfs인가? ㄴㄴ bfs인듯 ㄴㄴ 다익스트라

from heapq import heappush, heappop

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    shortest = [10**15]*(n+1)
    for i,j in edge:
        graph[i].append(j)
        graph[j].append(i)

    shortest[0] = 0
    shortest[1] = 0

    queue = []
    heappush(queue, [0,1])
    while queue:
        accum_dist, node = heappop(queue)
        for next_node in graph[node]:
            if accum_dist + 1 >= shortest[next_node]:
                continue
            shortest[next_node] = accum_dist + 1
            heappush(queue, [accum_dist+1, next_node])

    #print(shortest)
    #shortest.sort()

    return shortest.count(max(shortest))
