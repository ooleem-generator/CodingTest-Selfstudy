from collections import deque
#from heapq import heappush, heappop

def solution(priorities, location):
    queue = deque(priorities)
    queue_with_idx = deque()
    for idx, priority in enumerate(priorities):
        queue_with_idx.append((priority, idx))
    
    count = 0
    
    while queue:
        current_priority = max(queue)
        #print(queue)
        #print(queue_with_idx)
        p, i = queue_with_idx.popleft()
        queue.popleft()
        if p < current_priority:
            queue_with_idx.append((p, i))
            queue.append(p)
        else:
            count += 1
            if i == location:
                return count
        
    #print(queue)
    
    #return 0