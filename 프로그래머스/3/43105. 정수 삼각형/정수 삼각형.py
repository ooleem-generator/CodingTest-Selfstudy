def solution(triangle):
    dp = [[] for _ in range(len(triangle))]
    dp[0].append(triangle[0][0])
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 양쪽 끝은 그냥 내려간다
            # 나머지는 전의 합 결과를 비교한다
            if j == 0:
                dp[i].append(dp[i-1][j]+triangle[i][j])
            elif j == len(triangle[i])-1:
                dp[i].append(dp[i-1][j-1]+triangle[i][j])
            else:
                dp[i].append(max(dp[i-1][j-1]+triangle[i][j], dp[i-1][j]+triangle[i][j]))
    
    return max(dp[-1])