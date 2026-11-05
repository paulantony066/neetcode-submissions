class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        
        def combination(ind,ans,target,nums,ds):
            if ind==len(nums):
                if target==0:
                    ans.append(ds.copy())
                return
            if nums[ind]<=target:
                ds.append(nums[ind])
                combination(ind,ans,target-nums[ind],nums,ds)
                ds.pop()
            combination(ind+1,ans,target,nums,ds)
            
                
            

        ans=[]
        combination(0,ans,target,nums,[])

        return ans

                