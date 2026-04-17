class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid is greater than right, min is to the right of mid
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, min is at mid or to the left of mid
                right = mid
        
        return nums[left]  # left == right is the index of the min