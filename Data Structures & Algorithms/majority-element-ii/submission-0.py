class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        start=nums[0]
        left=0
        right=0

        while left<len(nums) and right<len(nums):
            count=0
            while right<len(nums) and nums[right]==start:
                count+=1
                right+=1
            if count>len(nums)//3:
                ans.append(start)
            if right<len(nums) and nums[right]!=start:
                start=nums[right]
            
        return ans
            

        
            

            
