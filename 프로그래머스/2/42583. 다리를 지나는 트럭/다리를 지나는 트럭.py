from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    truck_weights = deque(truck_weights)
    bridge.append([truck_weights.popleft(), 1])
    time = 1
    total_weight = bridge[0][0]
    
    while bridge:
        for truck in bridge:
            truck[1] += 1
            
        if bridge[0][1] > bridge_length:
            total_weight -= bridge.popleft()[0]
        
        if truck_weights and (total_weight + truck_weights[0]) <= weight:
            total_weight += truck_weights[0]
            bridge.append([truck_weights.popleft(), 1])
            
        time += 1
    
    return time