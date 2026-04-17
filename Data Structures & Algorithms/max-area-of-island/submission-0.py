class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if (min(r, c) < 0 or
                (r, c) in visit or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0
                ):
                return 0
            visit.add((r, c))
            max_found = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return max_found
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    res = max(res, dfs(r, c))
                

        return res



