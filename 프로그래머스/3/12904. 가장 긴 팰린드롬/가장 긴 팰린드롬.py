def solution(s):
    dp = [0]*len(s)
    string = ""
    for i in range(len(s)):
        string += s[i]
        for j in range(len(string)):
            target = string[j:]
            #print(string[j::-1])
            if target == target[::-1]:
                dp[j] = max(dp[j], len(target))
    
    #print(dp)
    
    return max(dp)