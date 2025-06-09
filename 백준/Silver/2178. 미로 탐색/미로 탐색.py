from collections import deque

n, m = map(int, input().split())
target = (n - 1, m - 1)
maze = [input() for _ in range(n)]
maze_available = [[] for _ in range(n)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for r in range(n):
    for c in range(m):
        if maze[r][c] == "1":
            maze_available[r].append([0, True])
        else:
            maze_available[r].append([0, False])

# print(maze_available)

maze_available[0][0][0] = 1


def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        curr_r, curr_c = queue.popleft()
        for dr, dc in direction:
            new_r, new_c = curr_r + dr, curr_c + dc
            if new_r < 0 or new_r >= n:
                continue
            elif new_c < 0 or new_c >= m:
                continue
            elif maze_available[new_r][new_c][1] == False:
                continue
            else:
                maze_available[new_r][new_c][1] = False
                maze_available[new_r][new_c][0] = maze_available[curr_r][curr_c][0] + 1
                queue.append((new_r, new_c))
                if (new_r, new_c) == target:
                    print(maze_available[new_r][new_c][0])


bfs((0, 0))