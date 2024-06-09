# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow is the midpoint
        first = head
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # separate lists
        second = slow.next
        slow.next = None
        
        # reverse second list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge both lists
        while prev:
            temp1, temp2 = first.next, prev.next
            first.next = prev
            prev.next = temp1
            first = temp1
            prev = temp2
