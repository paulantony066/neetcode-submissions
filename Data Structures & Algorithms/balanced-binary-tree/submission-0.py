# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        val=0
        def bal(root):
            nonlocal val
            if not root:
                return 0
            
            left_h=bal(root.left)
            right_h=bal(root.right)

            if abs(left_h-right_h)>1:
                val=-1
                
            return 1+max(left_h,right_h)
        bal(root)
        if val==-1:
            return False
        return True