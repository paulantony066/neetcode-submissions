class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change={5:0,10:0,20:0,0:float('inf')}

        if bills[0]>5:
            return False

        for i in range(len(bills)):
            bal_to_give=bills[i]-5
            if bal_to_give==15:
                if change[10]>=1 and change[5]>=1:
                    change[10]-=1
                    change[5]-=1
                elif change[5]>=3:
                    change[5]-=3
                else:
                    return False
            if bal_to_give==5:
                if change[5]>=1:
                    change[5]-=1
                else:
                    return False
            change[bills[i]]+=1
        return True

