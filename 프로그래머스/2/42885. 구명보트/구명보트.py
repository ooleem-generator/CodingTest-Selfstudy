# 50 70 80
# 50 50 70 80   120
#

from collections import deque

def solution(people, limit):
    count = 0
    people.sort()
    queue = deque(people)
    while len(queue) > 1:
        if queue[-1] + queue[0] > limit:
            queue.pop()
            count += 1
        else:
            queue.popleft()
            queue.pop()
            count += 1
        
    return count + len(queue)