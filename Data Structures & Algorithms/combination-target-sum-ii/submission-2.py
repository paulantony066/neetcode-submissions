class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        def combination(ind,ans,target,candidates,ds):

            
            if target==0:
                ans.append(ds.copy())
                return
            
            for i in range(ind,len(candidates)):
                if i > ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                ds.append(candidates[i])
                combination(i+1,ans,target-candidates[i],candidates,ds)
                ds.pop()

        ans=[]
        combination(0,ans,target,candidates,[])
        return ans
        

                
        