# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkValidity(root, minVal, maxVal):
            if not root:
                return True
            
            if root.val <= minVal or root.val >= maxVal:
                return False
            
            return checkValidity(root.left, minVal, root.val) and checkValidity(root.right, root.val, maxVal)

        return checkValidity(root, float('-inf'), float('inf'))