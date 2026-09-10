class Solution:
    def trap(self, height: List[int]) -> int:
        lmax=[0]*len(height)
        rmax=[0]*len(height)

        lmax[0]=height[0]
        lm=height[0]
        for i in range(1,len(height)):
            lm=max(height[i],lm)
            lmax[i]=lm
        rmax[0]=height[-1]
        rm=height[-1]
        for i in range(len(height)-1,-1,-1):
            rm=max(height[i],rm)
            rmax[i]=rm
        water=0
        for i in range(len(height)):
            pot=min(lmax[i],rmax[i])
            water=water+(pot-height[i])
        return water

        

