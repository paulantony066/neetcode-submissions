"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        arr=[]
        for i in intervals:
            temp=[]
            temp.append(i.start)
            temp.append(i.end)
            arr.append(temp)
        

        for i in range(1,len(arr)):
            if arr[i-1][1]>arr[i][0]:
                return False
        return True
