class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def comb(ind,arr,res,k,ds):
            
            if ind>=len(arr):
                if len(ds)==k:
                    res.append(ds.copy())
                return
            
            ds.append(arr[ind])
            comb(ind+1,arr,res,k,ds)
            ds.pop()
            comb(ind+1,arr,res,k,ds)
        arr=[]
        for i in range(1,n+1):
            arr.append(i)
        res=[]
        comb(0,arr,res,k,[])
        return res
