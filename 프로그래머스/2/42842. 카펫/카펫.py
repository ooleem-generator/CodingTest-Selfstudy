def solution(brown, yellow):
    
    product = brown+yellow
    plus = (brown+4)//2
    
    for i in range((plus//2)+1):
        if i*(plus-i) == product:
            height = i
            width = plus-i
    
    return [width, height]