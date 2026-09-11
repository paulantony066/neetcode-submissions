class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canship(cap):
            curr=cap
            ships=1
            for w in weights:
                if curr-w<0:
                    curr=cap
                    ships+=1
                curr-=w
            if ships<=days:
                return True
            else:
                return False


        l=max(weights)
        r=sum(weights)

        while l<=r:
            mid=(l+r)//2

            if canship(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans