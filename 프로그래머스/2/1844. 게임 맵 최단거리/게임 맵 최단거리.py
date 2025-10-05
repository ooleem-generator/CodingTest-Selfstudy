# 명심해라 최단거리는 BFS로 푼다.

from collections import deque

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque()
    queue.append([0,0])
    maps[0][0] = 0
    count = 1
    while queue:
        coordinates = len(queue)
        for _ in range(coordinates): # count 1회당 큐 안에 있는 좌표들에 대해서만 수행해야 하므로
            coordinate = queue.popleft()
            r,c = coordinate[0], coordinate[1]
            if (r == n-1) and (c == m-1):
                return count # 도착했으면 지금까지 간 거리 반환
            else:
                for d in direction:
                    newr = r+d[0]
                    newc = c+d[1]
                    if (0 <= newr < n) and (0 <= newc < m) and (maps[newr][newc] == 1):
                        queue.append([newr, newc])
                        maps[newr][newc] = 0
                        
        count += 1 # 1칸 진행
    
    return -1 # 도착점에 도달하지 못하고 큐가 빈 경우 -1 출력