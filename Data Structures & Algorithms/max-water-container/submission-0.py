class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        output_list = []
        for left in range(len(heights)):
            right = len(heights) - 1
            while left < right:
                min_num = min(heights[left], heights[right])
                dist = right - left
                output_list.append(min_num * dist)
                right -= 1
        
        return max(output_list)





        