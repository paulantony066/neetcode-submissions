"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        arr=[]
        for i in intervals:
            temp=[]
            temp.append(i.start)
            temp.append(i.end)
            arr.append(temp)
        
        curr=1
        start = sorted([i[0] for i in arr])
        end = sorted([i[1] for i in arr])

        s=0
        e=0
        max_room=0
        curr=0
        for i in range(len(start)):
            if start[s]<end[e]:
                curr+=1
                s+=1
            else:
                curr-=1
                e+=1
            max_room=max(curr,max_room)
        return max_room




        