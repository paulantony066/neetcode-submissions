class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

       

        if len(s)==1:
            return dic[s[0]]
        num=0
        prev=s[-1]
        num+=dic[prev]      
        

        for curr in range(len(s)-2,-1,-1):

            if dic[s[curr]]<dic[prev]:
                num-=dic[s[curr]]
                prev=s[curr]
                continue
            num+=dic[s[curr]]
            prev=s[curr]
        return num
            

            