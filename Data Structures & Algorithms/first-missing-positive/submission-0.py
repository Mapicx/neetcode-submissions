class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # [7,10,1,2,5]
        # [1, 2, 7, 10, 5]
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] <= 0 or nums[i] > n:
                i += 1
                continue
            
            index = nums[i] - 1
            if nums[index] != nums[i]:
                nums[i], nums[index] = nums[index], nums[i]
            else:
                i += 1
        for i, n in enumerate(nums):
            if i != n - 1:
                return i + 1
        return n + 1
            
