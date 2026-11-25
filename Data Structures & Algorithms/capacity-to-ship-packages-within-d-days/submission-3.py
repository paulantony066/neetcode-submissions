class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        def can_ship(cap):

            curr_cap=cap
            day=1

            for weight in weights:
                if curr_cap-weight<0:
                    day+=1
                    curr_cap=cap
                curr_cap=curr_cap-weight
            if day<=days:
                return True
            else:
                return False

        

        l=max(weights)

        r=sum(weights)


        ans=r

        while l<=r:
            mid=(l+r)//2

            if can_ship(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans