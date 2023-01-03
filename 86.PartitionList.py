# https://www.youtube.com/watch?v=KT1iUciJr4g
class Solution:
  def partition(self, head, x):
    left, right = ListNode(), ListNode()
    ltail, rtail = left, right
    
    while head:
      if head.val<x:
        ltail.next = head
        ltail=ltail.next
      else:
        rtail.next = head
        rtail = rtail.next
      head = head.next
      
    ltail.next = right.next
    rtail.next = None
    return left.next
    
        
