from functools import lru_cache
class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def recur(num):
            if num == 1:
                return 1
            res = 0 if num == n else num
            for i in range(1, num):
                res = max(res, (recur(i) * recur(num - i)))
            return res
        return recur(n)