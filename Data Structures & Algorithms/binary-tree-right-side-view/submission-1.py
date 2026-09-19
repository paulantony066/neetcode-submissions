# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        q=deque()

        if not root:
            return []
        
        q.append(root)
        while q:
            temp=[]
            for i in range(len(q)):
                node=q.popleft()
                temp.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
        ans=[]

        for i in res:
            ans.append(i[-1])
        return ans
        