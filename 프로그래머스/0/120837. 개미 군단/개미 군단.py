def solution(hp):
    j, hp1 = divmod(hp, 5)
    b, hp2 = divmod(hp1, 3)
    return j+b+hp2