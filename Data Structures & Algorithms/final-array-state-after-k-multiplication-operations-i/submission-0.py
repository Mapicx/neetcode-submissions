class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
        
        for _ in range(k):
            min_elem, index = heapq.heappop(heap)
            min_elem *= multiplier
            heapq.heappush(heap, (min_elem, index))
        
        heap = sorted(heap, key = lambda x: x[1])
        heap = [ele for ele, i in heap]
        return heap