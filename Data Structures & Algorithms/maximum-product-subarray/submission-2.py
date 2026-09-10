class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        prefix=[0]*len(nums)
        suffix=[0]*len(nums)

        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            if prefix[i-1]==0:
                prefix[i]=nums[i]
                continue
            prefix[i]=prefix[i-1]*nums[i]
        
        suffix[-1]=nums[-1]

        for i in range(len(nums)-2,-1,-1):
            if suffix[i+1]==0:
                suffix[i]=nums[i]
                continue
            suffix[i]=suffix[i+1]*nums[i]

        p=max(prefix)
        s=max(suffix)

        return max(s,p)
            
            
