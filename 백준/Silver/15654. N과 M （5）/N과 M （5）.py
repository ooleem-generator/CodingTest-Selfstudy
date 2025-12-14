n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))


selected = []


def backtrack(idx):
    if idx == m:
        print(" ".join(map(str, selected)))
        return

    for i in range(n):
        if nums[i] in selected:
            continue

        selected.append(nums[i])
        backtrack(idx + 1)
        selected.pop()


backtrack(0)