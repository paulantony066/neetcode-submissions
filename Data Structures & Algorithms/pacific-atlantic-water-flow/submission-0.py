class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        


        def dfs(r,c,seen,prev):
            if (r,c) in seen or r>=len(heights) or c>=len(heights[0]) or r<0 or c<0 or heights[r][c]<prev:
                return
            seen.add((r,c))
            dfs(r+1,c,seen,heights[r][c])
            dfs(r,c+1,seen,heights[r][c])
            dfs(r-1,c,seen,heights[r][c])
            dfs(r,c-1,seen,heights[r][c]) 
        
        
        r=len(heights)
        c=len(heights[0])

        pac=set()
        atl=set()

        rows=r
        #pacific top
        for i in range(c):
            dfs(0,i,pac,heights[0][i])
        #pacific bottom
        for i in range(r):
            dfs(i,0,pac,heights[i][0])

        for i in range(c-1,-1,-1):
            dfs(r-1,i,atl,heights[r-1][i])

        for i in range(r-1,-1,-1):
            dfs(i,c-1,atl,heights[i][c-1])

        res=[]

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in atl and (i,j) in pac:
                    res.append([i,j])
        return res