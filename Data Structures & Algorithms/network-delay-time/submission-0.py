class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph={}

        for src,target,time in times:
            if src not in graph:
                graph[src]=[]
                graph[src].append([target,time])
                continue
            graph[src].append([target,time])
        
        minheap=[(0,k)]
        seen={}

        while minheap:
            src_to_k,k=heapq.heappop(minheap)

            if k in seen:
                continue
                

            
            seen[k]=src_to_k
            
            for target,time in graph.get(k,[]):
                if target not in seen:
                    heapq.heappush(minheap,(time+src_to_k,target))
        if len(seen)!=n:
            return -1
        return max(seen.values())

