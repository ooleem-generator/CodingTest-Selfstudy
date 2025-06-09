import sys

input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
stack = [0]

tower_idx_finder = {v: i for i, v in enumerate(towers)}

for tower in towers:
    while stack[-1] <= tower:
        stack.pop()
        if stack == []:
            print(0, end=" ")
            stack.append(tower)
            break
    else:
        # print(towers.index(stack[-1]) + 1, end=" ")
        print(tower_idx_finder[stack[-1]] + 1, end=" ")
        stack.append(tower)