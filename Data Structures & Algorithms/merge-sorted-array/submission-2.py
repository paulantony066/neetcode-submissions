class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        l=len(nums1)-len(nums2)-1
        r=len(nums2)-1

        ind=len(nums1)-1

        while l>=0 and r>=0:
            if nums1[l]>nums2[r]:
                nums1[ind]=nums1[l]
                l-=1
            else:
                nums1[ind]=nums2[r]
                r-=1
            ind-=1

        while r>=0:
            nums1[ind]=nums2[r]
            r-=1
            ind-=1
            