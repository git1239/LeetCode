def reverseList(self, head):
        prev = None
        while head:
            prev, head.next, head = head, prev, head.next
        
        return prev
