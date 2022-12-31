# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = ''
        current = head
        while current != None:
            if current.val == 1: binary += '1'
            else: binary += '0'
            current = current.next
        return int(binary, 2)
