class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stck=[]
        for ass in asteroids:
            while stck and stck[-1]>0 and ass<0:
                if abs(stck[-1])>abs(ass):
                    break
                elif abs(stck[-1])<abs(ass):
                    stck.pop()
                    continue
                else:
                    stck.pop()
                    break
            else:
                stck.append(ass)

                

            
        return stck
                