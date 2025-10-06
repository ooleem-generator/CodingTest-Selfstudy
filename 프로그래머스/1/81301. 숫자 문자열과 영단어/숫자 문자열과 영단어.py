convert = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}

answer = []

def parsing(string):
    if not string[0].isdigit():
        for i in convert.keys():
            if string.startswith(i):
                answer.append(str(convert[i]))
    else:
         answer.append(string[0])    
    


def solution(s):
    for i in range(len(s)):
        parsing(s[i:])
    
    return int(''.join(answer))