class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        
        dic={}
        for num in hand:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1
        start=min(hand)
        dic[start]-=1
        total_groups = len(hand) // groupSize
        for i in range(total_groups):

            for i in range(groupSize-1):
                if start+1 in dic and dic[start+1]>0:
                    dic[start+1]-=1
                    start=start+1
                else:
                    return False
            minn=float('inf')
            for key,value in dic.items():
                if key<minn and value>0:
                    minn=key
            start=minn
            if start==float('inf'):
                break
            dic[start]-=1
        return True 




            

        


        

        


         
        

        