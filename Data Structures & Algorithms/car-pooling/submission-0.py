class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        arr=[0]*1001

        for cap,start,end in trips:
            arr[start]+=cap
            arr[end]-=cap

        res=0
        for i in arr:
            res+=i
            if res>capacity:
                return False
        return True