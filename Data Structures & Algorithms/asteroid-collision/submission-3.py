class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stck=[]

        for ass in asteroids:
            while stck and ass<0 and stck[-1]>0:
                diff=ass+stck[-1]

                if diff<0:
                    stck.pop()
                elif diff>0:
                    ass=0
                else:
                    stck.pop()
                    ass=0
            if ass:
                stck.append(ass)
        return stck
        
        
            