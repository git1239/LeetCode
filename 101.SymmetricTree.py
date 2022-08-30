class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root == None: 
            return True
        
        return self.dfs_solution(root.left,root.right)
    
    def dfs_solution(self,left,right):
        
        if left == None or right == None:
            return left == right
        if left.val != right.val:
            return False
        
        return self.dfs_solution(left.left,right.right) and self.dfs_solution(left.right,right.left)
