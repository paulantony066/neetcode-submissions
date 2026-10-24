class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res=0
        if sum(gas)<sum(cost):
            return -1
        
        l=0
        curr_gas=0
        diff=[0]*len(gas)
        for i in range(len(gas)):
            diff[i]=gas[i]-cost[i]


        while l<len(gas):
            curr_gas+=diff[l]
            if curr_gas<0:
                curr_gas=0
                res=l+1
            l+=1
            

        return res
