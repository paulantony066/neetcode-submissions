class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        q=deque()
        fresh=0
        rotten=0

        def rot_orange(r,c):
            nonlocal fresh
            if r<0 or c<0 or r==len(grid) or c==len(grid[0]) or grid[r][c]==0:
                return
            elif grid[r][c]==1:
                q.append((r,c))
                grid[r][c]=2
                fresh-=1
                

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    rotten+=1
                    q.append((i,j))

        if rotten==0 and fresh>0:
            return -1
        

        minute=0
        

        while q and fresh>0:
            minute+=1
            for i in range(len(q)):
                r,c=q.popleft()
                rot_orange(r+1,c)
                rot_orange(r,c+1)
                rot_orange(r-1,c)
                rot_orange(r,c-1)
        if fresh>0:
            return -1
        return minute




        