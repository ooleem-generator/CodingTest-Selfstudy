syntax = input()
number_list = [[]]
number_making = ""
for i in range(len(syntax)):
    if syntax[i].isnumeric():
        number_making += syntax[i]
    else:
        number_list[-1].append(int(number_making))
        number_making = ""
        if syntax[i] == "-":
            number_list.append([])
number_list[-1].append(int(number_making))
number_making = ""

number_0 = sum(number_list[0])
for i in range(1, len(number_list)):
    number_0 -= sum(number_list[i])


print(number_0)