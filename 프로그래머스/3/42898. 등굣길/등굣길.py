def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)] #i -> n, j -> m 
    
    for i,j in puddles:
        dp[j-1][i-1] = '0'
    
    #for i in range(m-1, -1, -1):
    dp[n-1][m-1] = 1
    
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            #print(f"current: {i},{j}")
            if i == n-1 and j == m-1:
                continue
            
            if dp[i][j] != '0':
                dp[i][j] = int(dp[i+1][j]) + int(dp[i][j+1])
                #print(dp[i][j])
    
    
    #print(dp)
    #answer = 0
    return dp[0][0]%1000000007