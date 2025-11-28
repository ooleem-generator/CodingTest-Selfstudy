def solution(participant, completion):
    marathon = {}
    for p in participant:
        if not marathon.get(p):
            marathon[p] = 1
        else:
            marathon[p] += 1
    for c in completion:
        marathon[c] -= 1
        
    return [m[0] for m in list(marathon.items()) if m[1] != 0].pop()