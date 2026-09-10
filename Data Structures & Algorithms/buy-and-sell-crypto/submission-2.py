class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=float('-inf')
        profit=0
        minprice=prices[0]

        if len(prices)==1:
            return 0

        for i in range(1,len(prices)):
            minprice=min(minprice,prices[i])
            maxprof=max(maxprof,prices[i]-minprice)
        return maxprof
            