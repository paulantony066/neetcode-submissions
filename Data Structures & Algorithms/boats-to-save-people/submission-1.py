class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left=0
        right=len(people)-1

        res=0

        while left<=right:
            remain=limit-people[right]
            res+=1
            right-=1
            if remain>=people[left]:
                left+=1
        return res