from functools import lru_cache
class Solution:
    def numSquares(self, n: int) -> int:
        @lru_cache(None)
        def recur(rem_amount):
            if rem_amount == 0:
                return 0
            res = rem_amount
            for i in range(1, rem_amount):
                if i * i > rem_amount:
                    break
                res = min(res, 1 + recur(rem_amount - i * i))
            return res
        return recur(n)
        