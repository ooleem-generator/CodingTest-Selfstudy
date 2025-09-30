n = int(input())
for _ in range(n):
    cent = int(input())
    q1, r1 = divmod(cent, 25)
    q2, r2 = divmod(r1, 10)
    q3, r3 = divmod(r2, 5)
    print(f"{q1} {q2} {q3} {r3}")