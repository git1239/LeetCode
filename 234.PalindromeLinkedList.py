# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        :type head: ListNode
        :rtype: bool

        Traverse each node in linked list, add value to array.

        Go through array using two pointers, if at any point they are not the same return false, if we make it to end of list return True

        Complexity: O(n + m) = O(n)
        Space: O(n) - Array
        """

        arr = []

        while head != None:
            arr.append(head.val)
            head = head.next

        # Check if its palindrome by using two pointers (one at start of array and one at end, comparing them as we go)
        l = 0
        r = len(arr) - 1;

        while l < r:
            if arr[l] != arr[r]:
                return False
            l = l + 1;
            r = r -1;
        return True
