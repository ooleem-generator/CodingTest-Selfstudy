h, w = map(int, input().split())
blocks = list(map(int, input().split()))
water = 0

max_block = max(blocks)
for i in range(1, max_block + 1):
    blk = []
    for idx, val in enumerate(blocks):
        if val >= i:
            blk.append(idx)
    # print(blk)
    if len(blk) > 1:
        for j in range(len(blk) - 1):
            water += blk[j + 1] - blk[j] - 1


print(water)