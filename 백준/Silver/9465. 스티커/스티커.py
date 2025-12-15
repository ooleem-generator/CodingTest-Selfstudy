t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0] * (n + 1), [0] * (n + 1)]
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))
    # dp[0][-1], dp[1][-1] = stickers[0][-1], stickers[1][-1]
    # dp[0][-2], dp[1][-2] = dp[1][-1]+stickers[0][-2], dp[0][-1]+stickers[1][-2]
    # for i in range(3, n+1, -1):
    #     dp[0][-i] = max()
    dp[0][1], dp[1][1] = stickers[0][-1], stickers[1][-1]
    for i in range(2, n + 1):
        dp[0][i] = stickers[0][-i] + max(dp[1][i - 2], dp[1][i - 1])
        dp[1][i] = stickers[1][-i] + max(dp[0][i - 2], dp[0][i - 1])

    # print(dp)
    print(max(dp[0][n], dp[1][n]))