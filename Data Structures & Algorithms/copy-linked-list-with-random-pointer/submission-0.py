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
        if not head:
            return None

        #insert copied nodes
        prun = head
        while prun:
            dummy = Node(prun.val, prun.next)
            prun.next = dummy
            prun = dummy.next

        #Assign random pointers
        prun = head
        while prun:
            if prun.random:
                prun.next.random = prun.random.next
            prun = prun.next.next

        #separate the two lists
        prun = head
        copy_head = head.next
        copy = copy_head
        while prun:
            prun.next = prun.next.next
            if copy.next:
                copy.next = copy.next.next
            prun = prun.next
            copy = copy.next

        return copy_head
