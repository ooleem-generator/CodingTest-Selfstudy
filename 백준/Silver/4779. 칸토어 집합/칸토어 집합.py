def kantor(n):
    if n == 0:
        return "-"
    else:
        return kantor(n - 1) + " " * (3 ** (n - 1)) + kantor(n - 1)


while True:
    try:
        print(kantor(int(input())))
    except:
        break