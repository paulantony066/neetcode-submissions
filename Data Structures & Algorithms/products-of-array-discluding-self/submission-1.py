class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[1]*len(nums)
        suff=[1]*len(nums)
        if len(nums)==1:
            return [0]
        prev=1
        for i in range(1,len(nums)):
            pref[i]=nums[i-1]*prev
            prev=nums[i-1]*prev

        prev=1
        for j in range(len(nums)-2,-1,-1):
            suff[j]=nums[j+1]*prev
            prev=nums[j+1]*prev
        arr=[]

        for i in range(len(nums)):
            arr.append(pref[i]*suff[i])
        return arr

            
