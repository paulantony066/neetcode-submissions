class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        dic={}

        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        sorted_pairs=sorted(dic.items(), key=lambda x:x[1])

        ptr=-1

        res=[]

        while k>0:
            res.append(sorted_pairs[ptr][0])
            ptr-=1
            k-=1
        return res

            
        
            