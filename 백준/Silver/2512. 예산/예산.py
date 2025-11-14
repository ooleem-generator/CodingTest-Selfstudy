#

n = int(input())
requests = list(map(int, input().split()))

budget = int(input())
requests.sort()

left = 0
right = requests[-1]

# 485보다 낮아야함

while left <= right:
    mid = (left + right) // 2
    summ = 0
    for r in requests:
        if r >= mid:
            summ += mid
        else:
            summ += r

    if budget < summ:
        right = mid - 1

    else:
        answer = mid
        left = mid + 1

print(answer)
