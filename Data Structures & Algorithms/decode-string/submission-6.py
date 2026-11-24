class Solution:
    def decodeString(self, s: str) -> str:
        stck=[]


        for i in range(len(s)):
            if s[i]!="]":
                stck.append(s[i])
            else:
                word=""
                while stck and stck[-1]!="[":
                    ch=stck.pop()
                    word=ch+word
                stck.pop()
                dig=""
                while stck and stck[-1].isdigit():
                    d=stck.pop()
                    dig=d+dig
                
                new_str=word*int(dig)
                stck.append(new_str)
        res=""
        for i in stck:
            res+=i
        return res
