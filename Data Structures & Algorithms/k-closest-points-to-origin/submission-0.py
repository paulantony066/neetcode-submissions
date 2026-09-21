class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic={}
        arr=[]
        for i in range(len(points)):
            temp=[]
            temp.append((0-points[i][0])**2+(0-points[i][1])**2,)
            temp.append(points[i][0])
            temp.append(points[i][1])
            arr.append(temp)
        heapq.heapify(arr)

        res=[]

        for i in range(k):
            ele=heapq.heappop(arr)
            res.append(ele)

        for i in range(len(res)):
            res[i]=res[i][1:]
        return res
        
