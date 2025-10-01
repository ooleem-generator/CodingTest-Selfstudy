a, b = list(map(int, input().split()))
alist = set(map(int, input().split()))
blist = set(map(int, input().split()))
print(len(alist) + len(blist) - 2 * len(alist.intersection(blist)))
