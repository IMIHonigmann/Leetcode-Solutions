"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        refMap = {}

        # 1st Pass: Create the nodes and assign them to the original nodes using a dict
        while cur:
            refMap[cur] = ListNode()
            refMap[cur].random = None
            refMap[cur].val = cur.val
            cur = cur.next

        # 2nd Pass: Link the nodes using the dict and use the dict to find the randompointer copy
        cur = head
        while cur:
            if cur.next:
                refMap[cur].next = refMap[cur.next]
            if cur.random:
                refMap[cur].random = refMap[cur.random]
            cur = cur.next
        
        if not head:
            return None
        return refMap[head]
