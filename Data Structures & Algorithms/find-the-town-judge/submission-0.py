class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming={}
        outgoing={}

        for i in range(1,n+1):
            incoming[i]=0
            outgoing[i]=0

        for i in range(len(trust)):
            out=trust[i][0]
            inc=trust[i][1]

            incoming[inc]+=1
            outgoing[out]+=1

        ans=-1

        for i in range(1,n+1):
            if incoming[i]==n-1 and outgoing[i]==0:
                return i
        return -1
            
