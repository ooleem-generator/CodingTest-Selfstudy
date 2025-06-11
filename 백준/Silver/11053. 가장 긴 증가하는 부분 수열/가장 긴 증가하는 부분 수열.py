n = int(input())
numbers = list(map(int, input().split()))
dp_table = [0] * n
for i in range(n - 1, -1, -1):
    candidate = []
    for j in range(i, n):
        if numbers[j] > numbers[i] or j == i:
            candidate.append(1 + dp_table[j])
    dp_table[i] = max(candidate)


print(max(dp_table))