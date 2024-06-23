# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Don't use a list. hashsets have constant lookup time while lists have linear lookup time
        cur = head
        nodeSet = set()

        while cur:
            if cur in nodeSet:
                return True
            nodeSet.add(cur)
            cur = cur.next

        return False
