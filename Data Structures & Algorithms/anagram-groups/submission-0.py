class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        op=[]
        for s in strs:
            srted=sorted(s)
            temp="".join(srted)

            if temp in dic:
                dic[temp].append(s)
            else:
                dic[temp]=[s]
        for key in dic:
            op.append(dic[key])

        return op
                
