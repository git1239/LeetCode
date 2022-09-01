# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        def helper(root,currsum=0):
            if root is None:
                return 0
            currsum+=root.val
            if not root.left and not root.right:
                return currsum==targetSum
            
            return helper(root.left,currsum) or helper(root.right,currsum)
        return helper(root)
