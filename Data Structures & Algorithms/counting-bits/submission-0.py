class Solution:
    def countBits(self, n: int) -> List[int]:

        op=[0]

        while len(op)<=n:
            l1=op.copy()
            for i in op:
                l1.append(i+1)
            op=l1


        return op[:n+1]