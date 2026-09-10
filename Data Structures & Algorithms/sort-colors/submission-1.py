class Solution:
    def sortColors(self, nums: List[int]) -> None:
        arr=[0]*3
        for i in nums:
            arr[i]+=1
        k=0
        for i in range(3):
            while arr[i]:
                nums[k]=i
                arr[i]-=1
                k+=1
        
            

        