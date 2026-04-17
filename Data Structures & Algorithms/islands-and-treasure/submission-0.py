class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        land_val = (2**31 - 1)
        ROWS, COLS = len(grid), len(grid[0])
        land = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                elif grid[r][c] == land_val:
                    land += 1
        length = 0
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        while queue and land > 0:
            for _ in range(len(queue)):
                curr_x, curr_c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = curr_x + dr, curr_c + dc
                    if (min(nc, nr) < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] != land_val
                        ):
                        continue
                    grid[nr][nc] = length+1
                    land -= 1
                    queue.append((nr, nc))
            length += 1



        

        
        