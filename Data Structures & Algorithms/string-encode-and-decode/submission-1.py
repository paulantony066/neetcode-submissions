class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for i in range(len(strs)):
            encoded += str(len(strs[i])) + "#" + strs[i]
        return encoded

    def decode(self, s: str) -> List[str]:
        res=[]
        
        ptr=0

        while ptr<len(s):
            start=ptr
            while s[start]!="#":
                start+=1
            num=int(s[ptr:start])
            start+=1
            word=s[start:start+num]

            res.append(word)

            ptr=start+num
            

        return res

