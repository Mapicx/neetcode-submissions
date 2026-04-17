from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: # odd sum cannot be divided equally we need only the even one
            return False
        total_sum = sum(nums)
        @lru_cache(None)
        def recur(i, curr_sum):
            if curr_sum == total_sum // 2:
                return True
            if curr_sum > total_sum // 2 or i == len(nums):
                return False
            
            return (
                recur(i+1, curr_sum) # either we skip it or
                or
                recur(i+1, curr_sum + nums[i]) # we take it 
            )

        return recur(0, 0)
        
        