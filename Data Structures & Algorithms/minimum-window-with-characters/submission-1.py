class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length=float('inf')
        found=0

        tdic={}
        for i in t:
            if i not in tdic:
                tdic[i]=1
            else:
                tdic[i]+=1
        
        sdic={}
        for i in t:
            if i not in sdic:
                sdic[i]=0
        
        l=0

        for r in range(len(s)):
            if s[r] in tdic:
                sdic[s[r]]+=1
                if sdic[s[r]]==tdic[s[r]]:
                    found+=1
            while found==len(tdic):
                if (r-l+1)<length:
                    start=l
                    end=r
                    length=(r-l+1)
                if s[l] in sdic:
                    sdic[s[l]]-=1
                    if sdic[s[l]]<tdic[s[l]]:
                        found-=1
                l+=1
        if length==float("inf"):
            return ""
        return s[start:end+1]
                
                


       
