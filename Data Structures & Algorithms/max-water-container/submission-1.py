class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        probable_output = -1
        for left in range(len(heights)):
            right = len(heights) - 1
            while left < right:
                min_num = min(heights[left], heights[right])
                dist = right - left
                probable_output = max(probable_output, (min_num * dist))
                right -= 1
        
        return probable_output





        