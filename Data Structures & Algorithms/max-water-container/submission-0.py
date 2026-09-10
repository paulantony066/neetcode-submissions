class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=float('-inf')

        left=0
        right=len(heights)-1

        while left<right:
            max_water=max(max_water,min(heights[left],heights[right])*(right-left))

            if heights[left]<heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            else:
                left+=1
                right-=1
        return max_water