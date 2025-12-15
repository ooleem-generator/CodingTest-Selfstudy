import sys

input = sys.stdin.readline

nalmuk = set()
n = int(input())
for _ in range(n):
    op_line = input().split()
    if len(op_line) == 2:
        op, number = op_line
        num = int(number)
    else:
        op = op_line[0]

    if op == "add":
        nalmuk.add(num)
    elif op == "remove":
        if num in nalmuk:
            nalmuk.remove(num)
    elif op == "check":
        if num in nalmuk:
            print(1)
        else:
            print(0)
    elif op == "toggle":
        if num in nalmuk:
            nalmuk.remove(num)
        else:
            nalmuk.add(num)
    elif op == "all":
        nalmuk = set(range(1, 21))
    elif op == "empty":
        nalmuk = set()

    # print(nalmuk)
