import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    employee_list = []
    for _ in range(n):
        a, b = map(int, input().split())
        employee_list.append((a, b))
    employee_list.sort()
    max_2 = n + 1
    count = 0
    for employee in employee_list:
        if employee[1] < max_2:
            max_2 = employee[1]
            count += 1

    print(count)