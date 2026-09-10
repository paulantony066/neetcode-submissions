class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set()
        for i in nums:
            seen.add(i)

        longest=0

        for i in range(len(nums)):
            n=nums[i]
            if n-1 not in seen:
                c=1
                while n+1 in seen:
                    c+=1
                    n+=1
                longest=max(longest,c)
        return longest
