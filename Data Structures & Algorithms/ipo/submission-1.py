class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxheap = []
        minheap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minheap)

        for _ in range(k):
            while minheap and minheap[0][0] <= w:
                c, p = heapq.heappop(minheap)
                heapq.heappush(maxheap, -p)
            
            if not maxheap:
                break
                
            profit = -1 * heapq.heappop(maxheap)

            w += profit
        
        return w

        