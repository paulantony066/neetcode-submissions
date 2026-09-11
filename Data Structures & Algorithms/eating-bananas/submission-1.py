class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def caneat(rate):
            time=0
            for banana in piles:
                time+=math.ceil(banana/rate)

            if time<=h:
                return True
            else:
                return False



        l=1
        r=max(piles)
        ans=0
        while l<=r:
            mid=(l+r)//2

            if caneat(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans


        