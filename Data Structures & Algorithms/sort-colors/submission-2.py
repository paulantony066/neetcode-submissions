class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        arr=[0]*3

        for i in nums:
            arr[i]+=1
        
        ptr=0

        for i in range(3):
            while arr[i]:
                nums[ptr]=i
                arr[i]-=1
                ptr+=1
                


        