class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inc={}
        out={}

        for src,dst in trust:
            if src in out:
                out[src]+=1
            else:
                out[src]=1
            if dst in inc:
                inc[dst]+=1
            else:
                inc[dst]=1

        for i in range(1,n+1):
            if inc.get(i,0)==n-1 and out.get(i,0)==0:
                return i
        return -1
        

        

        
