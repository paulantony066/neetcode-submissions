class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stck=[]

        for i in range(len(temperatures)):

            while stck and stck[-1][0]<temperatures[i]:
                days=i-stck[-1][1]
                res[stck[-1][1]]=days
                stck.pop()



            stck.append((temperatures[i],i))
        return res
            

