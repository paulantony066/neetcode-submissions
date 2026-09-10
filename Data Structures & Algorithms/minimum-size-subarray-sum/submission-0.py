class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length=float('inf')
        curr_sum=0

        left=0

        for right in range(len(nums)):
            curr_sum+=nums[right]
            while left<len(nums) and curr_sum>=target:
                min_length=min(min_length,right-left+1)
                curr_sum-=nums[left]
                left+=1
        if min_length!=float('inf'):
            return min_length
        return 0
