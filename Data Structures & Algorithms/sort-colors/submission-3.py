class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        

        arr=[0]*3

        for i in nums:
            arr[i]+=1

        lptr=0
        curr=0
        while lptr<len(nums):
            while arr[curr]!=0:
                nums[lptr]=curr
                lptr+=1
                arr[curr]-=1
            curr+=1
            
        