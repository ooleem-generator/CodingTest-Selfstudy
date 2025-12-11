n, m = map(int, input().split())

nums = list(range(1, n + 1))

def backtrack(start: int, chosen: list):
    # print(chosen)
    if len(chosen) == m:
        # for i in chosen:
        print(" ".join(chosen))
        return

    for i in range(start, len(nums)):
        chosen.append(str(nums[i]))
        backtrack(i + 1, chosen)
        chosen.pop()


backtrack(0, [])