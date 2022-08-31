class Solution:
    def minDepth(self, root):
        ans=[float('inf')]
        
        def solve(root,height):
            if not root:
                return 
            if not root.left and not root.right:
                ans[0]=min(ans[0],height)
                return
            
            solve(root.left,height+1)
            solve(root.right,height+1)
        
        solve(root,1)
        return ans[0] if ans[0]!=float('inf') else 0
