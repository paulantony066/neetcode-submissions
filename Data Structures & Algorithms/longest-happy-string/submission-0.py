class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:


        arr=[]
        res=""
        for cnt, char in [(a, "a"), (b, "b"), (c, "c")]:
            if cnt:
                heapq.heappush(arr, (-cnt, char))

        while arr:
            cnt,ch=heapq.heappop(arr)
            if len(res)>=2 and res[-1]==res[-2]==ch:
                if not arr:
                    break
                cnt2,ch2=heapq.heappop(arr)
                res+=ch2
                cnt2+=1

                if cnt2<0:
                    heapq.heappush(arr,(cnt2,ch2))
                
                heapq.heappush(arr,(cnt,ch))
            else:
                res+=ch
                cnt+=1
                if cnt<0:
                    heapq.heappush(arr,(cnt,ch))




        return res

