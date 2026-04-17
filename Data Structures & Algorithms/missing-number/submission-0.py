class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, x in enumerate(nums):
            res ^= i ^ x
        return res
