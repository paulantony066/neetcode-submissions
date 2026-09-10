class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        

        seen=set()
        for i in nums:
            seen.add(i)
        flag=0
        for ele in seen:
            if ele<0:
                flag=1
        if flag==1:
            start=1
            while True:
                if start not in seen:
                    return start
                start+=1
        
        else:
            
            start=1
            while True:
                if start not in seen:
                    return start
                start+=1






