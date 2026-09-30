class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj={}
        visited=set()

        def dfs(course):
            if course not in adj:
                return True
            if course in visited:
                return False
            if adj[course]==[]:
                return True    
            visited.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            adj[course]=[]
            return True

        for a,b in prerequisites:
            if a not in adj:
                adj[a]=[]
            if b not in adj:
                adj[b]=[]

            adj[a].append(b)

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        

