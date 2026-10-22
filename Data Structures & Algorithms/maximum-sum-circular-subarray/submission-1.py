class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        maxsum=nums[0]

        currsum=0

        for i in range(len(nums)):
            if currsum<0:
                currsum=0
            currsum+=nums[i]
            maxsum=max(currsum,maxsum)

        minsum=nums[0]
        currsum=0

        for i in range(len(nums)):
            if currsum>0:
                currsum=0
            currsum+=nums[i]
            minsum=min(minsum,currsum)
        res=max(maxsum,sum(nums)-minsum)
        if res!=0:
            return res
        return maxsum
