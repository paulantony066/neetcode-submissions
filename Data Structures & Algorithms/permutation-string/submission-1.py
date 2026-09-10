class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        win=len(s1)

        if len(s1)>len(s2):
            return False

        seen={}
        for i in s1:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1


        seen2={}

        for i in range(win):
            if s2[i] in seen2:
                seen2[s2[i]]+=1
            else:
                seen2[s2[i]]=1
        if seen==seen2:
            return True
        left=0
        for i in range(win,len(s2)):
            if s2[left] in seen2 and seen2[s2[left]]>0:
                seen2[s2[left]]-=1 
            if s2[left] in seen2 and seen2[s2[left]]==0:
                del seen2[s2[left]]

            if s2[i] in seen2:
                seen2[s2[i]]+=1
            else:
                seen2[s2[i]]=1
            left+=1

            if seen==seen2:
                return True
        return False