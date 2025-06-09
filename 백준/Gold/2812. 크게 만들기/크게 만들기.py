n, k = map(int, input().split())
number = input()

stack = []
erase_count = 0

for num in number:
    if erase_count == k:
        stack.append(int(num))
        # print(stack)
    else:
        if stack == []:
            stack.append(int(num))
            # print(stack)
        else:
            while True:
                if stack == [] or stack[-1] >= int(num) or erase_count == k:
                    break
                stack.pop()
                erase_count += 1
                # print(stack)
            stack.append(int(num))
            # print(stack)

while erase_count < k:
    stack.pop()
    erase_count += 1
            
[print(numb, end="") for numb in stack]