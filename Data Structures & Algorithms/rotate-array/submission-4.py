class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums.reverse()
        def rev(start,end):
            l=start
            r=end
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        k=k%len(nums)
        rev(0,k-1)
        rev(k,len(nums)-1)
        