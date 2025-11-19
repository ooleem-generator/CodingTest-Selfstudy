n, k = map(int, input().split())
temp = list(map(int, input().split()))

a = sum(temp[:k])
answer = a

if n > k:
    for i in range(0, n - k):
        a += temp[i + k] - temp[i]
        answer = max(a, answer)

print(answer)