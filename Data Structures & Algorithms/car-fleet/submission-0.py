class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        arr=[]

        for i in range(len(speed)):
            
            arr.append([position[i],speed[i],(target-position[i])/speed[i]])
            

        arr=sorted(arr ,key=lambda x:x[0],reverse=True)

        prev_fleet_time=0
        fleets=0

        for a in arr:
            if a[2]>prev_fleet_time:
                fleets+=1
                prev_fleet_time=a[2]
        return fleets


        
