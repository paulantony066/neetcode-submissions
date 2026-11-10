class Solution:

    def encode(self, strs: List[str]) -> str:

        enc=""
        for word in strs:
            ch=str(len(word))+"#"
            enc+=ch
            enc+=word
        return enc



    def decode(self, s: str) -> List[str]:

        ptr=0
        res=[]
        while ptr<len(s):
            cnt=""
            start=ptr
            while s[start]!="#":
                cnt+=s[start]
                start+=1
            l=int(cnt)
            res.append(s[start+1:start+1+l])
            ptr=start+1+l
        return res


