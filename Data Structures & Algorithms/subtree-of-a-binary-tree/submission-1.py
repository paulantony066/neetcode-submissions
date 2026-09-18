# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def same(tree1,tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 and tree2 or tree1 and not tree2:
                return False
            if tree1.val!=tree2.val:
                return False
            
            return same(tree1.left,tree2.left) and same(tree1.right,tree2.right)

        def is_sub(tree1,tree2):
            if not tree2:
                return True
            if not tree1:
                return False
            
            
            if same(tree1,tree2):
                return True
            
            return is_sub(tree1.left,tree2) or is_sub(tree1.right,tree2)

        return is_sub(root,subRoot)

        
        