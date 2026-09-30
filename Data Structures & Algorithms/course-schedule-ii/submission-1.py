class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        visited=set()
        done=set()

        adj={}

        res=[]

        def dfs(course):
            if course in done:
                return True
            
            if course in visited:
                return False

            visited.add(course)
            for pre in adj.get(course,[]):
                if not dfs(pre):
                    return False
            visited.remove(course)
            done.add(course)
            adj[course]=[]
            res.append(course)
            return True

        for a, b in prerequisites:
            if a not in adj:
                adj[a]=[]
            if b not in adj:
                adj[b]=[]

            adj[a].append(b)

        for i in range(numCourses):
            if not dfs(i):
                return []



        return res

        
        
        