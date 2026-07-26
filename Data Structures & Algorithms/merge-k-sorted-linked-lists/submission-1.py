# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        curr = res

        while True:
            minnode = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minnode == -1 or lists[minnode].val > lists[i].val:
                    minnode = i
                
            if minnode == -1:
                break
            curr.next = lists[minnode]
            lists[minnode] = lists[minnode].next
            curr = curr.next
        return res.next
