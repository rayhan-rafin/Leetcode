# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True

        def computeDepth (root):
            if root is None:
                return 0
            left_depth = computeDepth(root.left)
            right_depth = computeDepth(root.right)
            if (left_depth - right_depth) not in (-1,0,1):
                self.flag = False
            return max(left_depth,right_depth)+1
        computeDepth (root)
        return self.flag
