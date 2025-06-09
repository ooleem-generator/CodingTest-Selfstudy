n = int(input())
from collections import deque

tree = {}
preorder_stack = []
inorder_stack = []
postorder_stack = []

for _ in range(n):
    parent, left, right = input().split()
    visited = False
    tree[parent] = [left, right, visited]

# 트리 방문 초기화
def tree_clear(tree):
    for node in tree.keys():
        tree[node][2] = False


# 전위 순회
def preorder(tree, node):
    if not tree[node][2]:
        tree[node][2] = True
        preorder_stack.append(node)

    if tree[node][0] != ".":
        preorder(tree, tree[node][0])

    if tree[node][1] != ".":
        preorder(tree, tree[node][1])

#중위 순회
def inorder(tree, node):
    if tree[node][0] != ".":
        inorder(tree, tree[node][0])

    if not tree[node][2]:
        tree[node][2] = True
        inorder_stack.append(node)

    if tree[node][1] != ".":
        inorder(tree, tree[node][1])

#후위 순회
def postorder(tree, node):
    if tree[node][0] != ".":
        postorder(tree, tree[node][0])

    if tree[node][1] != ".":
        postorder(tree, tree[node][1])

    if not tree[node][2]:
        tree[node][2] = True
        postorder_stack.append(node)


preorder(tree, "A")
print("".join(preorder_stack))
tree_clear(tree)
inorder(tree, "A")
print("".join(inorder_stack))
tree_clear(tree)
postorder(tree, "A")
print("".join(postorder_stack))