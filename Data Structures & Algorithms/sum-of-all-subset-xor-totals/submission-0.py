class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
    

        def summ(i,total):

            if i+1>len(nums):
                return total
                
            return summ(i+1,total^nums[i])+summ(i+1,total)
        return summ(0,0)
            
            

            
