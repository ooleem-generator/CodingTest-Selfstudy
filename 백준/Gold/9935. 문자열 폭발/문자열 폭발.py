string = input()
explosive_string = input()

stack = []

for char in string:
    stack.append(char)
    if stack[-len(explosive_string) :] == list(explosive_string):
        for _ in range(len(explosive_string)):
            stack.pop()


if stack == []:
    print("FRULA")
else:
    for char in stack:
        print(char, end="")