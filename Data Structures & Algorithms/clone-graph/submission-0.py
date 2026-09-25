"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        stck=[]

        start=node

        stck.append(start)

        old_new={}

        seen=set()

        while stck:
            node=stck.pop()
            seen.add(node)
            old_new[node]=Node(val=node.val,neighbors=[])

            for nei in node.neighbors:
                if nei not in seen:
                    stck.append(nei)
                    seen.add(nei)
        

        for old,new in old_new.items():
            for nei in old.neighbors:
                newnode=old_new[nei]
                new.neighbors.append(newnode)

        return old_new[start]



