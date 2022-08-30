# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Explanation Inorder Traversal
        1. Traverse the left subtree ==> Inorder(left-subtree)
        2. Visit the root. for this problem we store root val in the result list 
        3. Traverse the right subtree ==> Inorder(right-subtree)
        4. return the result list
    """
    def helper(self, root, result):
        
        if root:
            self.helper(root.left, result)
            result.append(root.val)
            self.helper(root.right, result)
        
        return result
    
    def inorderTraversal(self, root):
        return self.helper(root, result=[])
