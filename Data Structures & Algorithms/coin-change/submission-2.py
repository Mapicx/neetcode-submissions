from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(amt):
            res = float('inf')
            if amt == 0:
                return 0
            for coin in coins:
                if amt - coin >= 0:
                    res = min(res, 1 + dfs(amt - coin))
            return res
        min_coins = dfs(amount)
        return -1 if min_coins == float('inf') else min_coins


        