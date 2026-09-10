class Solution:
    def isValid(self, s: str) -> bool:
        dic={
            "(":")",
            "[":"]",
            "{":"}"  }

        stack=[]
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                brac=stack.pop()
                if dic[brac]!=i:
                    return False
        if len(stack)!=0:
            return False
        return True