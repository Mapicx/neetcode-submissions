class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) - 1
        left = 0
        probable_output = -1
        while left < right:
            min_num = min(heights[left], heights[right])
            dist = right - left
            probable_output = max(probable_output, (min_num * dist))
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return probable_output