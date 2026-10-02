class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums)%2:
            return False

        dp=set()

        dp.add(0)

        for i in range(len(nums)):
            dpp=set()
            for subs in dp:
                dpp.add(subs+nums[i])
                dpp.add(subs)
            dp=dpp

        if sum(nums)//2 in dp:
            return True

        return False