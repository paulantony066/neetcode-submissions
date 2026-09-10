class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        if nums==[]:
            return []

        dic={}

        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        sorted_dic=sorted(dic.items(),key=lambda x:x[1])
        op=[]
        count=0
        for i in range(len(sorted_dic)-1,-1,-1):
            if count<k:
                op.append(sorted_dic[i][0])
                count+=1
            else:
                break
        return op
        
            

