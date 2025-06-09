import sys

input = sys.stdin.readline

n = int(input())
stack = [0]

for _ in range(n):
    stick = int(input())
    if stack[-1] > stick:
        stack.append(stick)
    else:
        while stack[-1] <= stick:
            stack.pop()
            if stack == []:
                break
        stack.append(stick)

print(len(stack))