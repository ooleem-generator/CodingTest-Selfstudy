from collections import deque
import sys

input = sys.stdin.readline

second = 0
snake = deque([(1, 1)])  # 첫번째가 행, 두번째가 열
apple = []
rotation = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
r_order = {}

n = int(input())
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    apple.append((a, b))
l = int(input())
for _ in range(l):
    a, b = input().split()
    r_order[int(a)] = b
    
while True:
    second += 1
    snake_next = (snake[-1][0] + rotation[0][0], snake[-1][1] + rotation[0][1])

    if (n + 1 in snake_next) or (0 in snake_next) or (snake_next in snake):
        print(second)
        break

    snake.append(snake_next)

    if snake[-1] in apple:
        apple.remove(snake[-1])
    else:
        snake.popleft()

    if second in r_order:
        if r_order[second] == "D":
            rotation.rotate(-1)
        else:
            rotation.rotate(1)