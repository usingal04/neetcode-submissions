# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxDia = [0]

        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)

            dia = left + right

            maxDia[0] = max(maxDia[0], dia)
        
            return 1 + max(left, right)
        
        height(root)
        return maxDia[0]