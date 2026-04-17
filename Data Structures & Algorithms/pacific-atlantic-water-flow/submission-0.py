class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        pacafic = set()
        atlantic = set()
        def dfs(r,c, visit, prevheight):
            if ((r, c) in visit or
                min(r,c) < 0 or
                r == ROWS or c == COLS or
                prevheight > heights[r][c]
                ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacafic, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])   

        for r in range(ROWS):
            dfs(r, 0, pacafic, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])        
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacafic and (r,c) in atlantic:
                        res.append([r, c])
        return res


        