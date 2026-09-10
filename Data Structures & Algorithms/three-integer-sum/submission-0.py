class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        n=len(nums)

        for i in range(len(nums)):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            offset=nums[i]
            low=i+1
            high=n-1
            while low<high:
                if offset+nums[low]+nums[high]==0:
                    res.append([offset,nums[low],nums[high]])
                    low+=1
                    high-=1
                    while low<high and nums[low]==nums[low-1]:
                        low+=1
                    while low<high and nums[high+1]==nums[high]:
                        high-=1
                elif offset+nums[low]+nums[high]<0:
                    low+=1
                else:
                    high-=1
        return res
                
                

