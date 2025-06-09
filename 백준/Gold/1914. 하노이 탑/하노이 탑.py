n = int(input())
print(2**n - 1)

if n <= 20:
    def hanoi(n, a, b):
        c = 6-a-b
        if n == 1:
            return f"{a} {b}\n"
        else:
            return hanoi(n - 1, a, c) + f"{a} {b}\n" + hanoi(n - 1, c, b)
    print(hanoi(n, 1, 3))