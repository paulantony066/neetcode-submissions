class Solution:
    def decodeString(self, s: str) -> str:
        stck=[]

        for ch in s:
            if ch=="]":
                word=""
                while stck and stck[-1]!="[":
                    c=stck.pop()
                    word=c+word
                stck.pop()
                dig=""
                while stck and stck[-1].isdigit():
                    d=stck.pop()
                    dig=d+dig
                times=int(dig)
                stck.append(word*times)
                continue



            stck.append(ch)
        return "".join(stck)
    

        