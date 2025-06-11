t = int(input())
bridge = []

for _ in range(t):
    w, e = map(int, input().split())
    bridge.append((w, e))
    # bridge.sort(key=lambda x: -x[1])

max_e = max([b[1] for b in bridge])
dp_table = [[0] * (max_e + 1) for _ in range(max_e + 1)]
for i in range(1, max_e + 1):
    dp_table[i][i] = 1
    dp_table[1][i] = i

# print(dp_table)
for i in range(2, len(dp_table)):
    for j in range(i + 1, len(dp_table)):
        dp_table[i][j] = dp_table[i - 1][j - 1] + dp_table[i][j - 1]

for west, east in bridge:
    print(dp_table[west][east])