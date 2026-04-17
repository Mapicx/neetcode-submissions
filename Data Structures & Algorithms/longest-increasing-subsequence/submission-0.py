from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache
        def recur(curr, prev):
            if curr == len(nums):
                return 0
            subseq = recur(curr + 1, prev) # do not include the element

            if prev == -1 or nums[curr] > nums[prev]:
                subseq = max(subseq, 1 + recur(curr + 1, curr)) # include the element
            return subseq
        
        return recur(0, -1)

            
            

        