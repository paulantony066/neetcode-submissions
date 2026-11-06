class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        

        def subsets(ind,arr,res,ds):
            if ind>=len(arr):
                res.add(tuple(ds.copy()))
                return
            
            ds.append(arr[ind])
            subsets(ind+1,arr,res,ds)
            ds.pop()
            subsets(ind+1,arr,res,ds)
        res=set()
        subsets(0,nums,res,[])
        op=[]

        for x in res:
            op.append(list(x))
        return op
