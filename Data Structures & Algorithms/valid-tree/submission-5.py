class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        adj={}
        visited=set()

        def dfs(node,nei):

            if node in visited:
                return False

            visited.add(node)
            for n in adj.get(node,[]):
                if n==nei:
                    continue
                if not dfs(n,node):
                    return False
            return True

        for a,b in edges:
            if a not in adj:
                adj[a]=[]
            if b not in adj:
                adj[b]=[]
            adj[a].append(b)
            adj[b].append(a)

        if not dfs(0, -1):
            return False

        if len(visited) != n:
            return False

        return True
        

        