class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()

        while n not in seen and n!=1:

            s=0
            seen.add(n)

            while n!=0:
                dig=n%10
                s+=dig*dig
                n=n//10
            n=s
        if n==1:
            return True
        return False
