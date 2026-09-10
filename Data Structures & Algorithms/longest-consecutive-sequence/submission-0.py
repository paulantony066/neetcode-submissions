class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set()
        ans=0
        for i in nums:
            seen.add(i)

        for i in nums:
            count=0
            if i-1 not in seen:
                num=i
                count=1
                while num+1 in seen:
                    count+=1
                    num=num+1

                ans=max(count,ans)
        return ans
        