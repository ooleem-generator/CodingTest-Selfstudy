import sys
input = sys.stdin.readline

n = int(input())
meetings = []
timetable = []
for _ in range(n):
    a, b = map(int, input().split())
    meetings.append((a, b, b - a))

meetings.sort(key=lambda x: (x[1], x[0]))
# print(meetings)
for meeting in meetings:
    if timetable == []:
        timetable.append(meeting)
    else:
        if meeting[0] >= timetable[-1][1]:
            timetable.append(meeting)

print(len(timetable))
