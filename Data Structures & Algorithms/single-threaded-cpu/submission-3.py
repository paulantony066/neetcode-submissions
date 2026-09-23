class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        
        res=[]

        

        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks=sorted(tasks, key=lambda x:x[0])


        minheap=[]
        time=tasks[0][0]

        ptr=0
        
        while len(res)<len(tasks) or minheap:
            while ptr<len(tasks) and time>=tasks[ptr][0]:
                heapq.heappush(minheap,[tasks[ptr][1],tasks[ptr][2]])
                ptr+=1
            if not minheap:
                time=tasks[ptr][0]
            else:
                t,ind=heapq.heappop(minheap)
                time+=t
                res.append(ind)
        return res


            

        