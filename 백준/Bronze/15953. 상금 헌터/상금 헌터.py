competition_1 = (
    [0] + [500] + [300] * 2 + [200] * 3 + [50] * 4 + [30] * 5 + [10] * 6 + [0] * 79
)
competition_2 = [0] + [512] + [256] * 2 + [128] * 4 + [64] * 8 + [32] * 16 + [0] * 33
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print((competition_1[a] + competition_2[b]) * 10000)
