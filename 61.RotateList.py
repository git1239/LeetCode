class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return
        l = 0
        p = head
        while p.next:
            l += 1
            p = p.next
        l += 1
        p.next = head
        i = l - k%l
        while i > 0:
            p = p.next
            i -= 1
        head = p.next
        p.next = None
        return head
