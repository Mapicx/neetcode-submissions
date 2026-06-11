class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = -1
        for n in nums:
            if n == candidate:
                count += 1
            else:
                if count == 0:
                    candidate = n
                else: 
                    count -= 1
        return candidate

