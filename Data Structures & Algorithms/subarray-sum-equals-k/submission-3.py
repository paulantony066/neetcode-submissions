class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={}

        curr_sum=0
        res=0

        for i in range(len(nums)):
            curr_sum+=nums[i]

            if curr_sum==k:
                res+=1



            diff=curr_sum-k

            if diff in dic:
                res+=dic[diff]

            if curr_sum in dic:
                dic[curr_sum]+=1
            else:
                dic[curr_sum]=1
        return res

            