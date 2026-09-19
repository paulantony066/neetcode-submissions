# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def inorder(curr,parent):
            left_parent=curr
            curr=curr.right
            while curr.left:
                left_parent=curr
                curr=curr.left
            return [curr,left_parent]

        
        if not root:
            return None

        curr=root
        parent=None

        while curr and curr.val!=key:
            if key>curr.val:
                parent=curr
                curr=curr.right
            else:
                parent=curr
                curr=curr.left
        if curr==None:
            return root

        #case 1 curr is leafnode:
        if curr.left==None and curr.right==None:
            if parent is None:
                return None
            if parent.left==curr:
                parent.left=None
            else:
                parent.right=None
            return root

        #case 2 
        if curr.left==None and curr.right or curr.right==None and curr.left:

            if curr.left:
                child=curr.left
            else:
                child=curr.right

            if parent is None:
                return child

            if parent.left==curr:
                parent.left=child
            else:
                parent.right=child

            return root

        
        #case 3

        res=inorder(curr,parent)
        leftsucc=res[0]
        leftparent=res[1]
        curr.val=leftsucc.val
        if leftparent.left==leftsucc:
            leftparent.left=leftsucc.right
        else:
            leftparent.right=leftsucc.right

        return root








