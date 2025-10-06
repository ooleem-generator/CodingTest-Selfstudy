def solution(n, arr1, arr2):
    arr = [str(bin(arr1[i] | arr2[i]))[2:] for i in range(n)]
    answer = []
    for b in arr:
        if len(b) < n:
            b = "0"*(n-len(b)) + b
        answer.append(b.replace('1', '#').replace('0', ' '))
    
    return answer