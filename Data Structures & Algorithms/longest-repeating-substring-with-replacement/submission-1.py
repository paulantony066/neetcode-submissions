class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        dic={}

        res=float('-inf')

        l=0
        replaced=0

        for r in range(len(s)):
            if s[r] in dic:
                dic[s[r]]+=1
            else:
                dic[s[r]]=1

            while (r-l+1)-max(dic.values())>k:
                dic[s[l]]-=1
                l+=1

            res=max(res,r-l+1)
        return res
            
