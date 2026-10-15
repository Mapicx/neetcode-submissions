import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            num, i = heapq.heappop(heap)
            num *= multiplier
            nums[i] = num
            heapq.heappush(heap, (num, i))

        return nums