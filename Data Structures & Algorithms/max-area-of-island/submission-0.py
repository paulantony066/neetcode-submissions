class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):
            if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0 or grid[i][j]==0:
                return 0
            else:
                area=1
                grid[i][j]=0
                area+=dfs(i+1,j)
                area+=dfs(i,j+1)
                area+=dfs(i-1,j)
                area+=dfs(i,j-1)
                return area

        res=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    res=max(res,dfs(i,j))
        return res
