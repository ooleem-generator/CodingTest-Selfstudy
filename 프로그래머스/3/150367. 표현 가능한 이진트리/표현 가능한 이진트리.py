# 7 = 111 (2)
# 42 = 0101010 (2) 32 8 2 0101011 1 0000000
# 5 = 101
# 4 = 100
# 8 = 100

# 111 = 64 32 8 4 2 1

# 95 = 64 16 8 4 2 1 1011111

# 2의 제곱수의 특징?

# 010
# 0000000 

def treecheck(string, isparent):
    length = len(string)
    
#     if length == 1:
#         if string = "1":
#             if not isparent:
#                 return 0
#         return 1
    
#     else:
    if string[length//2] == "1":
        if not isparent:
            return False
        else:
            if length == 1:
                return True
            else:
                return treecheck(string[:length//2], True) and treecheck(string[length//2+1:], True)
        
    else:
        if length == 1:
            return True
        else:
            return treecheck(string[:length//2], False) and treecheck(string[length//2+1:], False)
            
        
        
        

def solution(numbers):
    answer = []
    for num in numbers:
        string = str(bin(num)).lstrip('0b')
        length = len(string)
        target = 1
        while target <= length:
            target *= 2
        #print(string)
        string = "0"*(target-1-len(string)) + string
        
        #print(string)
        
        if string[len(string)//2] == "0":
            answer.append(0)
        else:
            answer.append(int(treecheck(string, True)))
        
    return answer