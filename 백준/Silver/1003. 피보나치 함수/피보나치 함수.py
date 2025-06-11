t = int(input())
dp_table = [[None] * 41 for _ in range(2)]  # r이 f(0),f(1)
dp_table[0][0] = 1
dp_table[1][0] = 0
dp_table[0][1] = 0
dp_table[1][1] = 1

# print(dp_table)


def dp(n):
    for i in range(2, n + 1):
        dp_table[0][i] = dp_table[0][i - 1] + dp_table[0][i - 2]
        dp_table[1][i] = dp_table[1][i - 1] + dp_table[1][i - 2]


order_list = [int(input()) for _ in range(t)]

dp(max(order_list))
for order in order_list:
    print(dp_table[0][order], dp_table[1][order])