from functools import lru_cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @lru_cache(None)
        def recur(rem_amount):
            if rem_amount == 0:
                return 1
            if rem_amount < 0:
                return 0
            
            tot_ways = 0
            for num in nums:
                tot_ways += recur(rem_amount - num)
            return tot_ways
        return recur(target)

        