# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def depth(root):
            if root is None:
                return 0
            left_depth = depth(root.left)  #curr node input
            right_depth = depth (root.right) #curr node input
            self.max_diameter = max (self.max_diameter, left_depth + right_depth) #checking
            return max(left_depth , right_depth)+1 #curr node output

        depth(root)
        return self.max_diameter
            
