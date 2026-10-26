class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res=[]
        for trip in triplets:
            if trip[0]>target[0] or trip[1]>target[1] or trip[2]>target[2]:
                continue
            res.append(trip)
        zero=0
        one=0
        two=0
        for trip in res:
            if target[0]==trip[0]:
                if zero==0:
                    zero+=1
                    
               
            if target[1]==trip[1]:
                if one==0:
                    one+=1
                
            if target[2]==trip[2]:
                if two==0:
                    two+=1
        if zero+one+two==3:
            return True
        return False
        
        
        
            