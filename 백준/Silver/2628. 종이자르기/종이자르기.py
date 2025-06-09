whole_width, whole_height = list(map(int, input().split()))
lines = int(input())
widths = []
heights = []
width_order = [0, whole_width]
height_order = [0, whole_height]
areas = []

for _ in range(lines):
    whflag, dotlinenumber = list(map(int, input().split()))
    if whflag:
        width_order.append(dotlinenumber)
    else:
        height_order.append(dotlinenumber)

width_order.sort()
height_order.sort()

for i in range(len(width_order) - 1):
    widths.append(width_order[i + 1] - width_order[i])

for i in range(len(height_order) - 1):
    heights.append(height_order[i + 1] - height_order[i])

for i in widths:
    for j in heights:
        areas.append(i * j)

print(max(areas))