from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        n = len(coins)
        @lru_cache(None)
        def recur(indx, rem_amt):
            nonlocal res
            if rem_amt == 0:
                return 1
            if rem_amt < 0 or indx == n:
                return 0
            take = recur(indx, rem_amt - coins[indx])
            skip = recur(indx + 1, rem_amt)
            return take + skip
        
        return recur(0, amount)

                


        