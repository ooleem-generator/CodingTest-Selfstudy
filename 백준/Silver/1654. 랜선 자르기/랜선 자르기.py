k, n = map(int, input().split())  # k는 10,000까지, n은 1,000,000까지
cables = [int(input()) for _ in range(k)]

cables.sort()

left = 1
right = cables[-1]

while True:
    if left > right:
        print(right)
        break
    mid = (left + right) // 2
    divided_cables = [cable // mid for cable in cables]  # 개수
    if (
        sum(divided_cables) < n
    ):  # 너무 몇개 안나온다 싶으면 -> 자르는 단위를 줄여야 한다
        right = mid - 1
    else:
        left = mid + 1