class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_ = 0
        min_size = float('inf')
        
        for right in range(len(nums)):
            sum_ += nums[right]
            
            while sum_ >= target:  # shrink window
                min_size = min(min_size, right - left + 1)
                sum_ -= nums[left]
                left += 1
        
        return 0 if min_size == float('inf') else min_size
