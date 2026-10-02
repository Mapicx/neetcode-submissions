from functools import lru_cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        @lru_cache() 
        def dfs(i):
            if i >= n:
                return 0
            res = float("-inf")
            for j in range(i, min((i+3), n)):
                res = max(res, (sum(stoneValue[i:j+1]) - dfs(j+1)))
            return res
        
        return "Alice" if dfs(0) > 0 else ("Bob" if dfs(0) < 0 else "Tie")