class Solution:
    def rob(self, nums: List[int]) -> int:
        

        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[1],nums[0])

        
        dp=[0]*len(nums)
        dp[1]=nums[1]

        for i in range(2,len(nums)):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        
        dp2=[0]*len(nums)
        dp2[0]=nums[0]
        dp2[1]=max(nums[0],nums[1])

        for i in range(2,len(nums)-1):
            dp2[i]=max(dp2[i-2]+nums[i],dp2[i-1])

        return max(max(dp),max(dp2))

