class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest=""
        first=strs[0]
        ptr=0
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        for i in range(len(strs[0])):
            ch=strs[0][i]
            for j in range(1,len(strs)):
                if i>=len(strs[j]) or strs[j][i]!=ch:
                    return longest
            longest+=ch
        return longest


            

