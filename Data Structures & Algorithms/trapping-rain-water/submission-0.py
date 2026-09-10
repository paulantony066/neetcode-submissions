class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[0]*len(height)
        rightmax=[0]*len(height)
        water=0
        leftmax[0]=height[0]

        for i in range(1,len(height)):
            leftmax[i]=max(height[i],leftmax[i-1])
        
        rightmax[-1]=height[-1]

        for i in range(len(height)-2,-1,-1):
            rightmax[i]=max(height[i],rightmax[i+1])

        for i in range(len(height)):
            potential=min(leftmax[i],rightmax[i])
            actual=potential-height[i]
            if actual>0:
                water+=actual
        return water
        