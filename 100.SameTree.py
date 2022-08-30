
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = []
            
        stack.append(p)
        stack.append(q)
        
        while(stack):
            
            a = stack.pop()
            b = stack.pop()
            
            if a == None and b == None:
                continue
            
            if(a != None and b == None) or (a == None and b != None) or (a.val != b.val):
                return False
            
            stack.append(a.left)
            stack.append(b.left)
            
            stack.append(a.right)
            stack.append(b.right)
        
        return True
