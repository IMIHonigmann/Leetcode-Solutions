# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def fastSlowPtrs(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        midpoint = None

        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            # when determining our midpoint for even numbers:
                # with the else: takes the first number of the two centered numbers -> mid is: [1,2,3,*4*,5,6,7,8]
                # without the else: takes the second number of the two centered numbers -> mid is: [1,2,3,4,*5*,6,7,8]
            # else:
            #     break
            slow = slow.next

        mid = slow
        print(mid)
