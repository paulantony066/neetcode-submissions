class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tdic={}
        found=0
        res=float('inf')
        ans=""


        for i in t:
            if i in tdic:
                tdic[i]+=1
            else:
                tdic[i]=1
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
                if (r-l+1)<res:
                    ans=s[l:r+1]
                    res=len(ans)
                if s[l] in tdic:
                    sdic[s[l]]-=1
                    if sdic[s[l]]<tdic[s[l]]:
                        found-=1
                l+=1
        return ans
                    
                
                





        