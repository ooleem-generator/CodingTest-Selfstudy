import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # n이 행, m이 열
checkboard = [[i for i in input()] for _ in range(n)]
count = 0
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for i in range(n):
    for j in range(m):
        moved_coord = [
            [i + d[0], j + d[1]]
            for d in direction
            if (0 <= i + d[0] < n) and (0 <= j + d[1] < m)
        ]
        # print(moved_coord)
        for mc in moved_coord:
            # print(checkboard[mc[0]][mc[1]])
            if checkboard[i][j] != checkboard[mc[0]][mc[1]]:
                break
        else:
            count += 1

print(2**count % (10**9 + 7))
