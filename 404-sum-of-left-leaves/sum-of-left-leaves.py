# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.s=0

        def dfs(root):
            if root is None:
                return 0
            if root.left:
                if root.left.left is None and root.left.right is None:
                    self.s+=root.left.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)

        return self.s
    
        