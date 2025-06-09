import sys

input = sys.stdin.readline

a_, b_, c_ = list(map(int, input().split()))


def super_remainder(a, b, c):
    if b == 1:
        return a % c
    else:
        if b % 2 == 1:
            return ((super_remainder(a, b // 2, c) ** 2) * super_remainder(a, 1, c)) % c
        else:
            return (super_remainder(a, b // 2, c) ** 2) % c


print(super_remainder(a_, b_, c_))
