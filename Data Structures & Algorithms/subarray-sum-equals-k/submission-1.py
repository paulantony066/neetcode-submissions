class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum=0
        dic={}
        c=0

        for i in range(len(nums)):
            curr_sum+=nums[i]
            diff=curr_sum-k

            if curr_sum==k:
                c+=1

            if diff in dic:
                c+=dic[diff]

            if curr_sum in dic:
                dic[curr_sum]+=1
            else:
                dic[curr_sum]=1
        return c