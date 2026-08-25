class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 0

        while curr and count < k:
            curr = curr.next
            count += 1

        if count < k:
            return head

        new_head = self.reverseKGroup(curr, k)
        prev = new_head
        curr = head

        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev