import math


def prime_list_maker(number):
    prime_list = [2]
    for i in range(3, number, 2):
        for prime in prime_list:
            if i % prime == 0:
                break
        else:
            prime_list.append(i)  # for 문 뒤의 else..
    return prime_list


prime_list = prime_list_maker(10000)

n = int(input())
for _ in range(n):
    num = int(input())
    for i in range(num // 2):
        if (num // 2) - i in prime_list and (num // 2) + i in prime_list:
            print(f"{(num//2)-i} {(num//2)+i}")
            break