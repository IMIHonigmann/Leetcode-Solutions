# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time Complexity O(2N)
        
        # Reverse List
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        dummy = ListNode()
        dummy.next = prev

        # Remove the node defined by n
        tail = dummy
        for i in range(1, n):
            tail = tail.next
        tail.next = tail.next.next

        # Remove the dummy node then reverse the list again to restore the order
        dummy = dummy.next
        while dummy:
            temp = dummy.next
            dummy.next = head
            head = dummy
            dummy = temp

        return head
