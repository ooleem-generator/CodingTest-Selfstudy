import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())  # m -> c, n -> r
    cabbage_map = [[0] * m for _ in range(n)]
    cabbage = []

    for _ in range(k):
        a, b = map(int, input().split())
        cabbage_map[b][a] = 1
        cabbage.append((b, a))

    count = 0

    def dfs(r, c):
        if 0 <= r < n and 0 <= c < m:
            if cabbage_map[r][c] == 0:
                return

            cabbage_map[r][c] = 0

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        else:
            return

    for i, j in cabbage:
        if cabbage_map[i][j] == 1:
            dfs(i, j)
            count += 1


    print(count)

