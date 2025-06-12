n = int(input())
max = n // 5
candidate = []
for i in range(max + 1):
    if (n - i * 5) % 2 == 0:
        candidate.append(i + (n - i * 5) // 2)
# print(candidate)
if candidate == []:
    print(-1)
else:
    print(min(candidate))