import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))

card.sort()

for num in search:
    left = 0
    right = len(card) - 1
    while True:
        if left > right:
            print(0, end=" ")
            break

        mid = (left + right) // 2
        if card[mid] > num:
            right = mid - 1
        elif card[mid] < num:
            left = mid + 1
        else:
            print(1, end=" ")
            break
