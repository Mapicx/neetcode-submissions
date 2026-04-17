class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid = heights
        ROWS, COLS = len(grid), len(grid[0])
        pacific = set()
        queue = deque()
        atlantic = set()
        res = []
        def bfs(r, c, visit):
            if (r,c) not in visit:
                queue.append((r,c))
                visit.add((r,c))
            dirs = [(0,1), (1,0), (-1,0), (0,-1)]
            while queue:
                for _ in range(len(queue)):
                    curr_x, curr_y = queue.popleft()
                    for dx, dy in dirs:
                        nx,ny = curr_x + dx, curr_y + dy
                        if (min(nx, ny) < 0 or
                            nx == ROWS or ny == COLS or
                            (nx, ny) in visit or
                            grid[curr_x][curr_y] > grid[nx][ny] 
                            ):
                            continue
                        queue.append((nx, ny))
                        visit.add((nx,ny))
        for c in range(COLS):
            bfs(0, c, pacific)
            bfs(ROWS - 1, c, atlantic)
        for r in range(ROWS):
            bfs(r, 0, pacific)
            bfs(r, COLS - 1, atlantic)  

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                        res.append([r, c])
        return res



        