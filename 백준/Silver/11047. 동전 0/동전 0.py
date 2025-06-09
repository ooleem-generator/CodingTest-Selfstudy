n, k = map(int, input().split())
answer = 0
coins = [int(input()) for _ in range(n)]
coins.reverse()
for coin in coins:
    if (k // coin) > 0:
        answer += k // coin
        k = k % coin

print(answer)