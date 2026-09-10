class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        arr=intervals
        arr.append(newInterval)

        arr.sort(key=lambda x:x[0])

        ans=[]
        ans.append(arr[0])

        for i in range(1,len(arr)):
            if arr[i][0]<=ans[-1][1]:
                ans[-1][1]=max(arr[i][1],ans[-1][1])
            else:
                ans.append(arr[i])
        return ans
