class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float('inf')

        currsum=0

        if sum(nums)<target:
            return 0

        l=0
        for r in range(len(nums)):


            currsum+=nums[r]

            while currsum>=target:
                res=min(res,r-l+1)
                currsum-=nums[l]
                l+=1

            
        return res