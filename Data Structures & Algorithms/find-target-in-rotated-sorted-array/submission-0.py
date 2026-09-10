class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l=0
        r=len(nums)-1
        res=float('inf')
        ind=0

        while l<=r:
            m=(l+r)//2


            if nums[m]<=nums[r]:
                if nums[m]<res:
                    res=nums[m]
                    ind=m
                r=m-1
            else:
                l=m+1
        if ind==0:
            l=0
            r=len(nums)-1
        else:
            #[3,4,5,6,1,2]
            if nums[0]<=target<=nums[ind-1]:
                l=0
                r=ind-1
            else:
                l=ind
                r=len(nums)-1
        
        while l<=r:
            m=(l+r)//2

            if target>nums[m]:
                l=m+1
            elif target<nums[m]:
                r=m-1
            else:
                return m
        return -1

            

            

        