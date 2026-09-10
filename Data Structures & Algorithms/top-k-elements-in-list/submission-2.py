class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}

        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1

        arr=sorted(dic,key=dic.get)
        ans=[]
        ptr=len(arr)-1
        while len(ans)<k:
            ans.append(arr[ptr])
            ptr-=1
        return ans

        