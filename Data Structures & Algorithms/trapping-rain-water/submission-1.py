class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftmax = 0
        rightmax = 0
        water = 0

        while left < right:
            if height[left] > leftmax:
                leftmax = height[left]
            
            if height[right] > rightmax:
                rightmax = height[right]
            
            if leftmax < rightmax:
                water += leftmax - height[left]
                left += 1
            else:
                water += rightmax - height[right]
                right -= 1
        
        return water