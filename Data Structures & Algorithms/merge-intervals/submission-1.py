class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])

        res=[]

        for interval in intervals:
            if not res:
                res.append(interval)
                continue
            
            top=res[-1]

            if top[1]>=interval[0]:
                newinterval=res.pop()
                res.append([top[0],max(top[1],interval[1])])
            else:
                res.append(interval)
        return res