counting = [0] * 26
players = []
n = int(input())
for _ in range(n):
    counting[ord(input()[0]) - 97] += 1

for i, v in enumerate(counting):
    if v >= 5:
        players.append(chr(i + 97))
if players == []:
    print("PREDAJA")
else:
    [print(i, end="") for i in players]