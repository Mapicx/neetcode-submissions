from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        res = []
        dq = deque()

        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            if (r - l + 1) == k:
                res.append(nums[dq[0]])
                l += 1
            if l > dq[0]:
                dq.popleft()
        return res

