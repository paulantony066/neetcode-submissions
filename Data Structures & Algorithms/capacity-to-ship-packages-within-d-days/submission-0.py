class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can(cap):
            ships=1
            capacity=cap

            for w in weights:
                if capacity-w<0:
                    ships+=1
                    capacity=cap

                capacity-=w

            return ships<=days
    



        l=max(weights)
        r=sum(weights)
        ans=r

        while l<=r:
            cap=(l+r)//2

            if can(cap):
                ans=min(ans,cap)
                r=cap-1
            else:
                l=cap+1
        return ans

