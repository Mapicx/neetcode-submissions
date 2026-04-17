class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach = 0
        i = 0
        n = len(nums)

        while True:
            if maxreach < i:
                return False
            maxreach = max(maxreach, i + nums[i])
            if maxreach >= n - 1:
                return True
            i += 1
