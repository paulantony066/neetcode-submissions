class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        

        seen=set()
        for i in nums:
            seen.add(i)
        start=1
        while True:
            if start not in seen:
                return start
            start+=1






