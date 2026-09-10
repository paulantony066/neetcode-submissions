class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stck=[]
        def push(x):
            stck.append(x)
        def add():
            stck.append(stck[-1]+stck[-2])
        def doubl():
            prev=stck[-1]
            stck.append(prev*2)
        def popp():
            stck.pop()
        
        for ele in operations:
            if ele=="+":
                add()
            elif ele=="D":
                doubl()
            elif ele=="C":
                popp()
            else:
                push(int(ele))
        return sum(stck)






        
