class Solution:
    def numDecodings(self, s: str) -> int:


        dp=[0]*len(s)+[0]

        if s[0]=="0":
            return 0

        dp[0]=1
        dp[1]=1

        for i in range(2,len(s)+1):
            onedigit=int(s[i-1])
            twodigit=int(s[i-2:i])

            if onedigit>=1:
                dp[i]+=dp[i-1]
            if twodigit>=10 and twodigit<=26:
                dp[i]+=dp[i-2]
        return dp[-1]





