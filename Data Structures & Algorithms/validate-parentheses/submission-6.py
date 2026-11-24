class Solution:
    def isValid(self, s: str) -> bool:
        dic={
            "(":")",
            "[":"]",
            "{":"}",
        }
        stck=[]
        for i in s:
            if i in dic:
                stck.append(i)
            else:
                if len(stck)==0:
                    return False
                brac=stck.pop()
                if dic[brac]!=i:
                    return False
        if len(stck)!=0:
            return False
        return True
                