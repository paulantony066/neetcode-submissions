class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[]

        r=len(word1)
        c=len(word2)

        for i in range(r+1):
            dp.append([0]*(c+1))

        for i in range(1,r+1):
            dp[i][0]=i

        for j in range(1,c+1):
            dp[0][j]=j

        w1='#'+word1
        w2='#'+word2

        for i in range(1,r+1):
            for j in range(1,c+1):
                if w1[i]!=w2[j]:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                else:
                    dp[i][j]=dp[i-1][j-1]
        return dp[-1][-1]
