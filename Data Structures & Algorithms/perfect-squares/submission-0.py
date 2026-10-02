class Solution:
    def numSquares(self, n: int) -> int:
        

        coins=[]

        square=1
        num=1

        while square<=n:
            coins.append(square)
            num+=1
            square=num*num

        
        dp=[0]*(n+1)
        dp[0]=0

        for i in range(1,n+1):
            minn=float('inf')

            for coin in coins:
                diff=i-coin
                if diff<0:
                    break
                minn=min(minn,dp[diff]+1)
            dp[i]=minn
        return dp[-1]