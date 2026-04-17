class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)] # -> elevation, r, c
        visit = set()

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            t, r, c = heapq.heappop(heap)

            if (r, c) in visit:
                continue
            
            if r == n -1 and c == n -1 :
                return t
            visit.add((r, c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) < 0 or
                    nr >= n or nc >= n or
                    (nr, nc) in visit
                    ):
                    continue
                nt = max(t, grid[nr][nc])
                heapq.heappush(heap, (nt, nr, nc))
        
        return 0
        