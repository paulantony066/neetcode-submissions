class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        for i in range(0,2**len(nums)):
            temp=[]
            b=bin(i)[2:].zfill(len(nums))
            for j in range(len(b)):
                if b[j]!="0":
                    temp.append(nums[j])
            res.append(temp)
        return res
                    
        