class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:

        if not head.next: return None                   # If only head, then it's the middle node

        ptr1, ptr2 = head.next, head                                       

        while ptr1.next and ptr1.next.next:             # On each iteration, ptr1 jumps two nodes and ptr2
            ptr1 = ptr1.next.next                       # jumps one node, so when ptr1 hits the end of the
            ptr2 = ptr2.next                            # list, ptr2 will be at the middle node.
      
        ptr2.next = ptr2.next.next                      # middle node is removed.

        return head
