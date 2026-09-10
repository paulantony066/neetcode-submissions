class Solution:
    def isValid(self, s: str) -> bool:
        stck=[]
        bracs=set("([{")
        dic={
            "(":")",
            "[":"]",
            "{":"}"
        }

        for ch in s:
            if ch in bracs:
                stck.append(ch)
            else:
                if len(stck)==0:
                    return False
                pair=stck.pop()
                if dic[pair]!=ch:
                    return False
        if len(stck)!=0:
            return False
        return True


