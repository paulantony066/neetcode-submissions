class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1={}
        dic2={}


        k=len(s1)
        if len(s1)>len(s2):
            return False

        for i in s1:
            if i in dic1:
                dic1[i]+=1
            else:
                dic1[i]=1
        
        for i in range(k):
            if s2[i] in dic2:
                dic2[s2[i]]+=1
            else:
                dic2[s2[i]]=1
        
        if dic1==dic2:
            return True
        l=0
        for i in range(k,len(s2)):
            if s2[l] in dic2 and dic2[s2[l]]>0:
                dic2[s2[l]]-=1
            if s2[l] in dic2 and dic2[s2[l]]==0:
                del dic2[s2[l]]
            
            if s2[i] in dic2:
                dic2[s2[i]]+=1
            else:
                dic2[s2[i]]=1
            
            if dic1==dic2:
                return True
            
            l+=1
        return False







