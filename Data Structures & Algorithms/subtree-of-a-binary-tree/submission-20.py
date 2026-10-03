# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkSame(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return checkSame(p.left, q.left) and checkSame(p.right, q.right)
        
        def checkSub(root):
            if not root:
                return False
            
            if checkSame(root, subRoot):
                return True
            
            return checkSub(root.left) or checkSub(root.right)
        
        return checkSub(root)