# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        res = ListNode()
        padding = ListNode()
        padding.next = res
        curres = res

        while cur1 and cur2:
            curres.val += cur1.val + cur2.val
            curres.next = ListNode()
            if curres.val > 9:
                curres.next.val = 1
                curres.val %= 10
            curres = curres.next
            padding = padding.next
            cur1 = cur1.next
            cur2 = cur2.next

        while cur1:
            curres.val += cur1.val
            curres.next = ListNode()
            if curres.val > 9:
                curres.next.val = 1
                curres.val %= 10
            curres = curres.next
            padding = padding.next
            cur1 = cur1.next
            
        while cur2:
            curres.val += cur2.val
            curres.next = ListNode()
            if curres.val > 9:
                curres.next.val = 1
                curres.val %= 10
            curres = curres.next
            padding = padding.next
            cur2 = cur2.next

        if padding.next.val == 0:
            padding.next = None

        return res
