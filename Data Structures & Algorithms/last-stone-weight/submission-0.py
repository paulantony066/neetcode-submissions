class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]

        heapq.heapify(stones)

        while len(stones)>1:
            stone1=heapq.heappop(stones)*-1
            stone2=heapq.heappop(stones)*-1

            bal=abs(stone1-stone2)

            heapq.heappush(stones,-bal)
        
        return -1*heapq.heappop(stones)

