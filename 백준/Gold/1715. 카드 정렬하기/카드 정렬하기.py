import sys
import heapq

input = sys.stdin.readline

nums = []
sums = []

n = int(input())  # n -> 100,000, 시간제한 2초

for _ in range(n):
    heapq.heappush(nums, int(input()))  # 이 작업에서 이미 O(nlog(n))

while len(nums) > 1:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    sums.append(a + b)
    heapq.heappush(nums, a + b)

print(sum(sums))