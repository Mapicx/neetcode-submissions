class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visit = set()
        res = 0
        heap = [(0, 0)]

        while heap:
            dst, pt = heapq.heappop(heap)
            if pt in visit:
                continue
            visit.add(pt)
            res += dst
            x1, y1 = points[pt]
            for nei in range(n):
                if nei not in visit:
                    x2, y2 = points[nei]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(heap, (dist, nei))
        return res
            

        