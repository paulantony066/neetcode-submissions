class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        q=deque()
        visit=set()

        def addroom(r,c):
            if r==len(grid) or c==len(grid[0]) or r<0 or c<0 or grid[r][c]==-1 or (r,c) in visit:
                return
            q.append((r,c))
            visit.add((r,c))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    q.append((i,j))
                    visit.add((i,j))

        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                addroom(r+1,c)
                addroom(r,c+1)
                addroom(r-1,c)
                addroom(r,c-1)
            dist+=1

