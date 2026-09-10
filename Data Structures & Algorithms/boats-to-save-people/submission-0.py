class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        min_boat=0

        left=0
        right=len(people)-1

        while left<=right:
            remain=limit-people[right]
            right-=1
            min_boat+=1
            if left<=right and people[left]<=remain:
                left+=1
                
        return min_boat












        





        