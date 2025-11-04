n = int(input())
dp = [0] * (n + 1)
dp[1] = 0
for i in range(2, n + 1):
    candidate = []
    if i % 3 == 0:
        candidate.append(dp[i // 3] + 1)
    if i % 2 == 0:
        candidate.append(dp[i // 2] + 1)

    candidate.append(dp[i - 1] + 1)

    dp[i] = min(candidate)
    # print(dp)

print(dp[n])