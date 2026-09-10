class Solution:
    def sortColors(self, nums: List[int]) -> None:

        q = collections.Counter(nums)

        nums[:] = [0] * q[0] + [1] * q[1] + [2] * q[2]
        