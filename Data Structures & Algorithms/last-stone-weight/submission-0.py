class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            if x == y:
                continue
            elif x < y:
                res = -(y - x)
                heapq.heappush(max_heap, res)
            elif y < x:
                res = -(x - y)
                heapq.heappush(max_heap, res)
        if len(max_heap) > 0:
            return -heapq.heappop(max_heap)
        return 0
        

        