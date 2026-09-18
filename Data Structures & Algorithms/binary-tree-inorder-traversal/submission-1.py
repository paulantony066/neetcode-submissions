# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stck=[]
        res=[]
        curr=root
        while True:
            if curr!=None:
                stck.append(curr)
                curr=curr.left
            else:
                if len(stck)==0:
                    break
                node=stck.pop()
                res.append(node.val)
                curr=node.right
        return res


                

        
        
