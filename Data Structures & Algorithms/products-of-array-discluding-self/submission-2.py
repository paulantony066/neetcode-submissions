class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left=[0]*len(nums)


        currsum=nums[0]
        left[0]=1

        for i in range(1,len(nums)):
            left[i]=currsum
            currsum*=nums[i]
        
        currsum=nums[-1]
        right=[0]*len(nums)
        right[-1]=1
        for i in range(len(nums)-2,-1,-1):
            right[i]=currsum
            currsum*=nums[i]
        
        res=[]

        for i in range(len(nums)):
            res.append(right[i]*left[i])
        return res

        
            
            



