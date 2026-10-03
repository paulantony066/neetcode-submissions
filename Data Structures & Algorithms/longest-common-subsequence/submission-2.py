class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        



        dp=[]

        for i in range(len(text1)+1):
            dp.append([0]*(len(text2)+1))

        x2='#'
        x2+=text1

        y2='#'
        y2+=text2

        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if x2[i]==y2[j]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            
        return dp[-1][-1]  