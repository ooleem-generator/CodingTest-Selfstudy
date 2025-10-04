from collections import deque

def solution(progresses, speeds):
    integrated = deque()
    for i in range(len(progresses)):
        integrated.append([progresses[i], speeds[i]])
    answer = []
    while integrated:
        features = 0
        for task in integrated:
            task[0] += task[1]
        while integrated and integrated[0][0] >= 100:
            integrated.popleft()
            features += 1
        if features > 0:
            answer.append(features)
        
        
    return answer