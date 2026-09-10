class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0
        left=0
        right=len(heights)-1
        lmax=0
        rmax=0
        while left<right:
            b=min(heights[left],heights[right])
            ans=max(ans,b*(right-left))
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
            
        return ans