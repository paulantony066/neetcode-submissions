class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastind={}

        for i in range(len(s)):
            lastind[s[i]]=i
        res=[]
        end=0
        size=0

        for i in range(len(s)):
            size+=1
            end=max(end,lastind[s[i]])

            if i==end:
                res.append(size)
                size=0
        return res


        
        



