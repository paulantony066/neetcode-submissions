class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res=0
        adj={}
        visited=set()

        def dfs(node):
            if adj[node]==[]:
                return
            if node in visited:
                return

            visited.add(node)
            for nei in adj.get(node,[]):
                dfs(nei)

        
        for a,b in edges:
            if a not in adj:
                adj[a]=[]
            if b not in adj:
                adj[b]=[]

            adj[a].append(b)
            adj[b].append(a)

        for i in range(n):
            if i not in adj:
                res+=1
                continue
            if i not in visited:
                dfs(i)
                res+=1
        return res