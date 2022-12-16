class Solution(object):
    def removeNodes(self, head):
        if not head.next:
            return head
        nextNode = self.removeNodes(head.next)
        if head.val < nextNode.val:
            return nextNode
        else:
            head.next = nextNode 
            return head
