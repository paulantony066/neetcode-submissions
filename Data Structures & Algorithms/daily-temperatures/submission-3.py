class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res=[0]*len(temperatures)
        stck=[]

        for i in range(len(temperatures)):
            while stck and temperatures[i]>stck[-1][0]:
                temp=stck.pop()
                diff=i-temp[1]

                res[temp[1]]=diff
            
            stck.append((temperatures[i],i))
        return res
