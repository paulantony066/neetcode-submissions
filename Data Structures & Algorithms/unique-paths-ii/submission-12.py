class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        

        m=len(obstacleGrid)

        n=len(obstacleGrid[0])

        


        dp=obstacleGrid

        if dp[0][0]==1:
            return 0
        
        flag=0
        for i in range(m):
            if flag==1:
                dp[i][0]=0
                continue
            elif dp[i][0]!=1:
                dp[i][0]=1
            else:
                dp[i][0]=0
                flag=1
        flag=0
        for j in range(1,n):
            if flag==1:
                dp[0][j]=0
                continue
            elif dp[0][j]!=1:
                dp[0][j]=1
            else:
                dp[0][j]=0
                flag=1

        for i in range(1,m):
            for j in range(1,n):
                if dp[i][j]==1:
                    dp[i][j]=0
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]

        return dp[m-1][n-1]
            
