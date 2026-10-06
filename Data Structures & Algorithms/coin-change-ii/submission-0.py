class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp=[]
        
        for i in range(len(coins)):
            dp.append([0]*(amount+1))



        for i in range(len(coins)):
            dp[i][0]=1

        for i in range(1,amount+1):
            if i%coins[0]==0:
                dp[0][i]=1
            else:
                dp[0][i]=0
            

        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                if coins[i]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    diff=j-coins[i]
                    dp[i][j]=dp[i-1][j]+dp[i][diff]
        return dp[-1][-1]
