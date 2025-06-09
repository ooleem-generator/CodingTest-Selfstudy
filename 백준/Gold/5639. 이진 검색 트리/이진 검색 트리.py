import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline
binary_tree = []


def pre_post_converter(tree):
    root = []
    left = []
    right = []
    for i in range(len(tree)):
        if i == 0:
            root.append(tree[i])
        else:
            if tree[i] < tree[0]:
                left.append(tree[i])
            else:
                right.append(tree[i])
    if len(left) >= 2:
        left = pre_post_converter(left)
    if len(right) >= 2:
        right = pre_post_converter(right)
    return left + right + root


while True:
    try:
        binary_tree.append(int(input()))

    except:
        converted_tree = pre_post_converter(binary_tree)
        [print(tree) for tree in converted_tree]
        break