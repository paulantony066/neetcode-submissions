class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftsum=[0]*len(nums)
        rightsum=[0]*len(nums)
        if len(nums)==1:
            return 0
        if len(nums)==0:
            return 0

        summ=1
        for i in range(len(nums)):
            leftsum[i]=summ
            summ*=nums[i]
        summ=1
        for j in range(len(nums)-1,-1,-1):
            rightsum[j]=summ
            summ*=nums[j]

        op=[]

        for i in range(len(nums)):
            op.append(leftsum[i]*rightsum[i])
        return op


