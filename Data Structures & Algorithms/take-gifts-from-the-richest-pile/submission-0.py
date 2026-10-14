import math
import heapq
class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest_gift = -heapq.heappop(max_heap)
            remaining = math.isqrt(largest_gift)
            heapq.heappush(max_heap, -remaining)

        return -sum(max_heap)
