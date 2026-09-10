class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=""

        for word in strs:
            cnt=str(len(word))
            enc+=cnt+"#"+word
        return enc

        
            


    def decode(self, s: str) -> List[str]:
        arr=[]
        ptr=0
        while ptr<len(s):
            cnt=""
            while s[ptr]!="#":
                cnt+=s[ptr]
                ptr+=1
            c=int(cnt)
            ptr+=1
            word=s[ptr:ptr+c]
            arr.append(word)
            ptr=ptr+c
        return arr
            





        
