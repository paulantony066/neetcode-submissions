class Solution:
    def jump(self, nums: List[int]) -> int:
        
        l=0
        r=0
        res=0

        while r<len(nums)-1:
            max_reach=0
            for i in range(l,r+1):
                max_reach=max(max_reach,i+nums[i])
            l=r+1
            r=max_reach
            res+=1
        return res